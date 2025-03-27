from flask import Blueprint, render_template, request, flash, redirect, url_for
from servicio.insumo import InsumoServicio
from formularios.agregar_insumo import Agregar_Insumo
from bd import bd
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('insumo', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))

@controlador.route('/insumos')
@login_required
@trabajador_permission.require(http_exception=403)
def insumos():
    insumo_servicio = InsumoServicio(bd)
    medidas = insumo_servicio.obtener_medidas()
    insumos = insumo_servicio.obtener_insumos()
    inventarios = insumo_servicio.obtener_inventario_insumos()
    return render_template('insumos.html', inventarios=inventarios, insumos=insumos, medidas=medidas)

@controlador.route('/insumos_crear', methods=['GET', 'POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def crear_insumo():
    form = Agregar_Insumo(request.form)
    if request.method == 'POST':
        insumo_servicio = InsumoServicio(bd)
        insumo = insumo_servicio.agregar_insumo(request.form)
        flash("Insumo creado exitosamente.", "success")
        return redirect(url_for('insumo.insumos'))
    return render_template('agregar_insumo.html', form=form)