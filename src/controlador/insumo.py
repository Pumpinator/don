from flask import Blueprint, render_template
from servicio.insumo import InsumoServicio
from bd import bd
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('controlador_insumo', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))

@controlador.route('/insumos')
@login_required
@comprador_permission.require(http_exception=403)
def insumos():
    insumo_servicio = InsumoServicio(bd)
    insumos = insumo_servicio.obtener_insumos()
    return render_template('insumos.html', insumos=insumos)