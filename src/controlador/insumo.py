from flask import Blueprint, render_template, request, flash, redirect, url_for
from servicio.cocina import CocinaServicio
from servicio.inventario import InventarioServicio
from formularios.agregar_insumo import AgregarInsumo
from bd import bd
from flask_login import login_required
from datetime import date
from flask_principal import Permission, RoleNeed

controlador = Blueprint('insumo', __name__)

trabajador_permission = Permission(RoleNeed('TRABAJADOR'))

@controlador.route('/insumos_inventario')
@login_required
@trabajador_permission.require(http_exception=403)
def insumos_inventario():
    inventario_servicio = InventarioServicio(bd)
    inventarios = inventario_servicio.obtener_insumos_inventarios()
    rol = 'inventario'
    return render_template('insumo/insumos.html',rol=rol, inventarios=inventarios)


@controlador.route('/insumos')
@login_required
@trabajador_permission.require(http_exception=403)
def insumos():
    inventario_servicio = InventarioServicio(bd)
    insumos = inventario_servicio.obtener_insumos()
    rol = 'insumos'
    return render_template('insumo/insumos.html', rol=rol, insumos=insumos)



@controlador.route('/insumos_detalles/<int:insumo_id>')
@login_required
@trabajador_permission.require(http_exception=403)
def insumos_detalles(insumo_id):
    hoy = date.today()
    inventario_servicio = InventarioServicio(bd)
    insumos = inventario_servicio.obtener_detalles_insumo(insumo_id)
    for insumo in insumos:
        if insumo['caducidad']:
            diferencia = hoy - insumo['caducidad']
            insumo['caducado'] = diferencia.days > 30
    return render_template('insumo/insumo_detalles.html', insumos=insumos, hoy=hoy)

@controlador.route('/insumos/crear', methods=['GET', 'POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def crear_insumo():
    form = AgregarInsumo(request.form)
    if request.method == 'POST' and form.validate_on_submit():  # Validar el formulario
        cocina_servicio = CocinaServicio(bd)
        cocina_servicio.agregar_insumo(request.form)
        flash("Insumo creado exitosamente.", "success")
        return redirect(url_for('principal.insumo.insumos'))
    elif request.method == 'POST':
        flash("Por favor, corrige los errores en el formulario.", "danger")
    return render_template('insumo/agregar_insumo.html', form=form)

@controlador.route('/insumos_editar/<int:id>', methods=['GET', 'POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def insumos_editar(id):
    inv_servicio = InventarioServicio(bd)
    insumo = inv_servicio.obtener_insumo(id=id)
    form = AgregarInsumo(obj=insumo)
    if request.method == 'POST' and form.validate_on_submit():
        inv_servicio.editar_insumo(form, id=id)
        flash("Insumo editado exitosamente.", "success")
        return redirect(url_for('principal.insumo.insumos'))
    elif request.method == 'POST':
        flash("Por favor, corrige los errores en el formulario.", "danger")
    return render_template('insumo/editar_insumo.html', form=form, insumo=insumo)