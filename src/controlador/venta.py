from flask import Blueprint, render_template, request, redirect, url_for
from servicio.venta import VentaServicio
from formularios.venta import VentaForm
from bd import bd
from servicio.inventario import InventarioServicio
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('venta', __name__)

trabajador_permission = Permission(RoleNeed('TRABAJADOR'))

@controlador.route('/ventas', methods=['GET', 'POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def ventas():
    form = VentaForm()
    inventario_servicio = InventarioServicio(bd)
    inventarios = inventario_servicio.obtener_galletas()
    if form.validate():
        venta_servicio = VentaServicio(bd)
        venta_servicio.generar_venta(form.data)
        return redirect(url_for('venta.ventas'))
    return render_template('ventas.html', form=form, inventarios=inventarios)