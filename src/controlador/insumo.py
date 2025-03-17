from flask import Blueprint, render_template
from servicio.insumo import obtener_insumos

controlador = Blueprint('controlador_insumo', __name__)

@controlador.route('/insumos')
def insumos():
    insumos = obtener_insumos()
    return render_template('insumos.html', insumos=insumos)