from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from flask_principal import Permission, RoleNeed
from flask import Blueprint, render_template, request, redirect, url_for
from bd import bd
from modelo.galleta import Galleta
from modelo.insumo import Insumo
from modelo.medida import Medida
from modelo.receta import Receta
from modelo.ingrediente import Ingrediente
from flask_login import login_required
from flask_principal import Permission, RoleNeed
from servicio.produccion import ProduccionServicio
from servicio.receta import RecetaServicio

controlador = Blueprint('receta', __name__)

# Permisos
admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

# Ruta para mostrar las recetas
@controlador.route('/recetas', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def recetas():
    receta = RecetaServicio(bd)
    recetas = receta.obtener_recetas()
    print(recetas)
    return render_template('receta/recetas.html', recetas=recetas)

# Ruta para crear una receta
@controlador.route('/receta/crear', methods=['POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def crear_receta():
    try:
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        galleta_id = request.form['galleta_id']
        procedimiento = request.form['procedimiento']
        
        # Obtener los arrays de insumos, cantidades y medidas
        insumo_ids = request.form.getlist('insumo_id[]')
        cantidades = request.form.getlist('cantidad[]')
        medida_ids = request.form.getlist('medida_id[]')
        
        # Llamar al servicio para crear la receta
        produccion_servicio = ProduccionServicio(bd)
        produccion_servicio.crear_receta(nombre, galleta_id, procedimiento, insumo_ids, cantidades, medida_ids)

        # Mostrar mensaje de éxito
        flash("Receta creada exitosamente.", "success")
        return redirect(url_for('principal.receta.recetas'))
    
    except Exception as e:
        flash(f"Error al crear la receta: {str(e)}", "danger")
        return redirect(url_for('principal.receta.recetas'))

# Ruta para editar una receta
@controlador.route('/receta/editar/<int:receta_id>', methods=['POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def editar_receta(receta_id):
    try:
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        galleta_id = request.form['galleta_id']
        procedimiento = request.form['procedimiento']
        
        # Obtener los arrays de insumos, cantidades y medidas
        insumo_ids = request.form.getlist('insumo_id[]')
        cantidades = request.form.getlist('cantidad[]')
        medida_ids = request.form.getlist('medida_id[]')
        
        # Llamar al servicio para editar la receta
        produccion_servicio = ProduccionServicio(bd)
        produccion_servicio.editar_receta(receta_id, nombre, galleta_id, procedimiento, insumo_ids, cantidades, medida_ids)

        # Mostrar mensaje de éxito
        flash("Receta editada exitosamente.", "success")
        return redirect(url_for('principal.receta.recetas'))
    
    except Exception as e:
        flash(f"Error al editar la receta: {str(e)}", "danger")
        return redirect(url_for('principal.receta.recetas'))
