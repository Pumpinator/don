from flask import Blueprint, render_template
from servicio.usuario import UsuarioServicio
from bd import bd

controlador = Blueprint('controlador_usuario', __name__)

@controlador.route('/usuarios')
def usuarios():
    usuario_servicio = UsuarioServicio(bd)
    usuarios = usuario_servicio.obtener_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)
