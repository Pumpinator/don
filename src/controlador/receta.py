from flask import Blueprint, render_template
from sqlalchemy import text
from servicio.produccion import ProduccionServicio
from bd import bd
from flask_login import login_required
from flask_principal import Permission, RoleNeed
from flask import Blueprint, render_template, request, redirect, url_for
from modelo.galleta import Galleta
from modelo.insumo import Insumo
from modelo.medida import Medida
from modelo.receta import Receta
from modelo.ingrediente import Ingrediente
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('receta', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))
admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))


@controlador.route('/recetas', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def recetas():
    return render_template('receta/recetas.html')

@controlador.route('/receta/crear', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def crear_receta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        galleta_id = request.form['galleta_id']
        procedimiento = request.form['procedimiento']
        
        # Obtener arrays de insumos, cantidades y medidas
        insumo_ids = request.form.getlist('insumo_id[]')
        cantidades = request.form.getlist('cantidad[]')
        medida_ids = request.form.getlist('medida_id[]')
        
        # Convertir a cadenas separadas por comas
        insumos_str = ','.join(insumo_ids)
        cantidades_str = ','.join(cantidades)
        medidas_str = ','.join(medida_ids)

        # Llamar al procedimiento almacenado
        query = text("CALL SP_InsertarReceta(:nombre, :galleta_id, :procedimiento, :insumos, :cantidades, :medidas)")
        bd.session.execute(query, {
            'nombre': nombre,
            'galleta_id': galleta_id,
            'procedimiento': procedimiento,
            'insumos': insumos_str,
            'cantidades': cantidades_str,
            'medidas': medidas_str
        })
        bd.session.commit()

        return redirect(url_for('principal.receta.recetas'))
    
    # Obtener datos para el formulario
    galletas = bd.session.query(Galleta).all()
    insumos = bd.session.query(Insumo).all()
    medidas = bd.session.query(Medida).all()
    return render_template('receta/crear_receta.html', 
                         galletas=galletas, 
                         insumos=insumos, 
                         medidas=medidas)