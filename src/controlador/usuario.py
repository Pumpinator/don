from flask import Blueprint, render_template
from servicio.usuario import obtener_usuarios

controlador = Blueprint('controlador_usuario', __name__)

@controlador.route('/usuarios')
def usuarios():
    usuarios = obtener_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)