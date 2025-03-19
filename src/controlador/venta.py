from flask import Blueprint, render_template, request, redirect, url_for
from servicio.venta import generar_venta
from formularios.venta import VentaForm
from bd import bd
from servicio.galleta import GalletaServicio

controlador = Blueprint('controlador_venta', __name__)

@controlador.route('/ventas', methods=['GET', 'POST'])
def ventas():
    form = VentaForm()
    servicio = GalletaServicio(bd)
    inventarios = servicio.obtener_inventarios()
    if form.validate_on_submit():
        generar_venta(form.data)
        return redirect(url_for('controlador_venta.ventas'))
    return render_template('ventas.html', form=form, inventarios=inventarios)