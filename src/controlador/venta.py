from flask import Blueprint, render_template, request, redirect, url_for
from servicio.venta import generar_venta
from formularios.venta import VentaForm
from modelo.galleta import Galleta

controlador = Blueprint('controlador_venta', __name__)

@controlador.route('/ventas', methods=['GET', 'POST'])
def ventas():
    form = VentaForm()
    galletas = Galleta.query.all()
    if form.validate_on_submit():
        generar_venta(form.data)
        return redirect(url_for('controlador_venta.ventas'))
    return render_template('ventas.html', form=form, galletas=galletas)