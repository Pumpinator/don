from flask import Blueprint, render_template
from servicio.galleta import GalletaServicio
from bd import bd

controlador = Blueprint('controlador_galleta', __name__)

@controlador.route('/galletas')
def galletas():
    servicio = GalletaServicio(bd)
    galletas = servicio.obtener_galletas()
    return render_template('galletas.html', galletas=galletas)