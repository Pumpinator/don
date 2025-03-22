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
@trabajador_permission.require(http_exception=403)
def insumos():
    insumo_servicio = InsumoServicio(bd)
    medidas = insumo_servicio.obtener_medidas()
    insumos = insumo_servicio.obtener_insumos()
    inventarios = insumo_servicio.obtener_inventario_insumos()
    return render_template('insumos.html', inventarios=inventarios, insumos=insumos, medidas=medidas)