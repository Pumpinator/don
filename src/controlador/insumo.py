from flask import Blueprint, render_template, request, flash, redirect, url_for
from servicio.cocina import CocinaServicio
from servicio.inventario import InventarioServicio
from formularios.agregar_insumo import AgregarInsumo
from bd import bd
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('insumo', __name__)

trabajador_permission = Permission(RoleNeed('TRABAJADOR'))

@controlador.route('/insumos')
@login_required
@trabajador_permission.require(http_exception=403)
def insumos():
    cocina_servicio = CocinaServicio(bd)
    inventario_servicio = InventarioServicio(bd)
    medidas = cocina_servicio.obtener_medidas()
    insumos = cocina_servicio.obtener_insumos()
    inventarios = inventario_servicio.obtener_insumos()
    return render_template('insumo/insumos.html', inventarios=inventarios, insumos=insumos, medidas=medidas)

@controlador.route('/insumos/crear', methods=['GET', 'POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def crear_insumo():
    form = AgregarInsumo(request.form)
    if request.method == 'POST':
        cocina_servicio = CocinaServicio(bd)
        insumo = cocina_servicio.agregar_insumo(request.form)
        flash("Insumo creado exitosamente.", "success")
        return redirect(url_for('insumo.insumos'))
    return render_template('insumo/agregar_insumo.html', form=form)