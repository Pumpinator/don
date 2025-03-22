from flask import Blueprint, render_template
from servicio.usuario import UsuarioServicio
from bd import bd
from flask_login import login_required
from flask_principal import Permission, RoleNeed


controlador = Blueprint('controlador_usuario', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))

@controlador.route('/usuarios')
@login_required
@admin_permission.require(http_exception=403)
def usuarios():
    usuario_servicio = UsuarioServicio(bd)
    usuarios = usuario_servicio.obtener_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)
