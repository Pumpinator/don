from flask import Blueprint, render_template
from servicio.cocina import CocinaServicio
from servicio.inventario import InventarioServicio
from bd import bd
from datetime import date
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('galleta', __name__)

admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

@controlador.route('/galletas')
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def galletas():
    inventario_servicio = InventarioServicio(bd)
    inventarios = inventario_servicio.obtener_galletas()
    print(inventarios)
    return render_template('galletas/galletas.html', inventarios=inventarios)

@controlador.route('/galletas_agregar')
@login_required
@trabajador_permission.require(http_exception=403)
def galletas_agregar():
    
    return render_template('galletas/galletas_agregar.html')


@controlador.route('/galletas_detalles/<int:galleta_id>')
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