from flask import Blueprint, render_template
from servicio.galleta import GalletaServicio
from bd import bd
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('controlador_galleta', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))


@controlador.route('/galletas')
@login_required
@trabajador_permission.require(http_exception=403)
def galletas():
    servicio = GalletaServicio(bd)
    galletas = servicio.obtener_galletas()
    return render_template('galletas.html', galletas=galletas)