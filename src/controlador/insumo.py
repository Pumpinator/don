from flask import Blueprint, render_template
from servicio.insumo import InsumoServicio
from bd import bd

controlador = Blueprint('controlador_insumo', __name__)

@controlador.route('/insumos')
def insumos():
    insumoservicio = InsumoServicio( bd )
    insumos = insumoservicio.obtener_insumos()
    inventario = insumoservicio.obtener_inventario()
    return render_template('insumos.html', insumos=insumos, inventario=inventario)