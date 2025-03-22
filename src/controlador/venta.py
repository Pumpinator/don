from flask import Blueprint, render_template, request, redirect, url_for
from servicio.venta import VentaServicio
from formularios.venta import VentaForm
from bd import bd
from servicio.galleta import GalletaServicio
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('controlador_venta', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))

@controlador.route('/ventas', methods=['GET', 'POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def ventas():
    form = VentaForm()
    galleta_servicio = GalletaServicio(bd)
    inventarios = galleta_servicio.obtener_inventarios()
    if form.validate():
        venta_servicio = VentaServicio(bd)
        venta_servicio.generar_venta(form.data)
        return redirect(url_for('controlador_venta.ventas'))
    return render_template('ventas.html', form=form, inventarios=inventarios)