from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required
from flask_principal import Permission, RoleNeed
import bd
from servicio.compra import CompraServicio
from bd import bd

controlador = Blueprint('compra', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))
admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

@controlador.route('/compras')
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def compras():
    compra_servicio = CompraServicio(bd)
    return render_template('compras.html')
