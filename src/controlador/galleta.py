from flask import Blueprint, render_template
from servicio.cocina import CocinaServicio
from servicio.inventario import InventarioServicio
from bd import bd
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('galleta', __name__)

trabajador_permission = Permission(RoleNeed('TRABAJADOR'))

@controlador.route('/galletas')
@login_required
@trabajador_permission.require(http_exception=403)
def galletas():
    cocina_servicio = CocinaServicio(bd)
    inventario_servicio = InventarioServicio(bd)
    galletas = cocina_servicio.obtener_galletas()
    inventarios = inventario_servicio.obtener_galletas()
    return render_template('galletas.html', galletas=galletas, inventarios=inventarios)