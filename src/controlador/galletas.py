from flask import Blueprint, render_template
from servicio.galleta import obtener_galletas

controlador = Blueprint('controlador_galleta', __name__)

@controlador.route('/galletas')
def galletas():
    galletas = obtener_galletas()
    return render_template('galletas.html', galletas=galletas)