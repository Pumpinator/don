from flask import Blueprint, flash, redirect, render_template, request, url_for, current_app
from servicio.cocina import CocinaServicio
from servicio.inventario import InventarioServicio
from bd import bd
from formularios.agregar_galleta import AgregarGalleta, EditarGalleta
from datetime import date
from flask_login import login_required
from flask_principal import Permission, RoleNeed
import os
from werkzeug.utils import secure_filename

controlador = Blueprint('galleta', __name__)

admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

@controlador.route('/galletas/inventarios')
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def galletas_inv():
    inventario_servicio = InventarioServicio(bd)
    inventarios = inventario_servicio.obtener_galletas_inv()
    return render_template('galletas/galletas_inv.html', inventarios=inventarios)

@controlador.route('/galletas')
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def galletas():
    inventario_servicio = InventarioServicio(bd)
    inventarios = inventario_servicio.obtener_galletas()
    print(inventarios)
    return render_template('galletas/galletas.html', inventarios=inventarios)

@controlador.route('/galletas/agregar', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def galletas_agregar():
    form = AgregarGalleta()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            if 'imagen' not in request.files or request.files['imagen'].filename == '':
                flash("La imagen es obligatoria.", "danger")
                return render_template('galletas/galletas_agregar.html', form=form)

            imagen = request.files['imagen']
            filename = secure_filename(imagen.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            imagen.save(filepath)  

            cocina_servicio = CocinaServicio(bd)
            data = {
                'nombre': form.nombre.data,
                'precio': form.precio.data,
                'imagen': filename  
            }
            cocina_servicio.agregar_galletas(data)

            flash("Galleta creada exitosamente.", "success")
            return redirect(url_for('principal.galleta.galletas'))
        except ValueError as e:
            flash(str(e), "danger")
    return render_template('galletas/galletas_agregar.html', form=form)


@controlador.route('/galleta/<int:galleta_id>')
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def galletas_detalles(galleta_id):
    hoy = date.today()
    inventario_servicio = InventarioServicio(bd)
    detalles = inventario_servicio.detalles_galleta(galleta_id)
    for galleta in detalles:
        if galleta['caducidad']:
            diferencia = hoy - galleta['caducidad']
            galleta['caducada'] = diferencia.days > 7
    return render_template('galletas/galletas_detalles.html', detalles=detalles, id=id)