from flask import Blueprint, render_template
from flask_login import login_required
from flask_principal import Permission, RoleNeed
import bd
from servicio.compra import CompraServicio

controlador = Blueprint('compra', __name__)

trabajador_permission = Permission(RoleNeed('TRABAJADOR'))

@controlador.route('/compras', methods=['GET', 'POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def compras():
    compra_servicio = CompraServicio(bd)
    return render_template('compras.html')