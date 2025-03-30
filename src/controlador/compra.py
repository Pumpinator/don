from flask import Blueprint, render_template
from flask_login import login_required
from flask_principal import Permission, RoleNeed
from servicio.compra import CompraServicio # Usar el servicio de compra para manejar la lógica
from flask_principal import Permission, RoleNeed
from bd import bd

controlador = Blueprint('compra', __name__)

admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

@controlador.route('/compras')
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def compras():
    compra_servicio = CompraServicio(bd)
    return render_template('compras.html')
