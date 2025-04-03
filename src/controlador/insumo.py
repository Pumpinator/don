from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from servicio.cocina import CocinaServicio
from servicio.inventario import InventarioServicio
from formularios.agregar_insumo import AgregarInsumo
from bd import bd
from flask_login import login_required
from datetime import date
from flask_principal import Permission, RoleNeed

controlador = Blueprint('insumo', __name__)

admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

@controlador.route('/insumos/<string:modulo>')
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def insumos(modulo):
    inventario_servicio = InventarioServicio(bd)
    if modulo == 'inventarios':        
        inventarios = inventario_servicio.obtener_insumos_inventarios()
        return render_template('insumo/insumos.html',rol=modulo, inventarios=inventarios)
    elif modulo == 'tipos':
        inventario_servicio = InventarioServicio(bd)
        insumos = inventario_servicio.obtener_insumos()
        return render_template('insumo/insumos.html', rol=modulo, insumos=insumos)
    else:
        abort(404)

@controlador.route('/insumos/inventarios/<int:insumo_id>')
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def insumos_detalles(insumo_id):
    hoy = date.today()
    inventario_servicio = InventarioServicio(bd)
    insumos = inventario_servicio.obtener_detalles_insumo(insumo_id)
    for insumo in insumos:
        if insumo['caducidad']:
            diferencia = hoy - insumo['caducidad']
            insumo['caducado'] = diferencia.days > 7
    return render_template('insumo/insumo_detalles.html', insumos=insumos, hoy=hoy, insumo_id=insumo_id)

@controlador.route('/insumos/crear', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def crear_insumo():
    form = AgregarInsumo(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        try:
            cocina_servicio = CocinaServicio(bd)
            cocina_servicio.agregar_insumo(request.form)
            flash("Insumo creado exitosamente.", "success")
            return redirect(url_for('principal.insumo.insumos', modulo='tipos'))
        except ValueError as e:
            flash(str(e), "danger")
    elif request.method == 'POST':
        flash("Por favor, corrige los errores en el formulario.", "danger")
    return render_template('insumo/agregar_insumo.html', form=form)

@controlador.route('/insumos/tipos/<int:insumo_id>', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def insumos_editar(insumo_id):
    inv_servicio = InventarioServicio(bd)
    insumo = inv_servicio.obtener_insumo(insumo_id)
    form = AgregarInsumo(obj=insumo)
    if request.method == 'POST' and form.validate_on_submit():
        try:
            inv_servicio.editar_insumo(form, insumo_id)
            flash("Insumo editado exitosamente.", "success")
            return redirect(url_for('principal.insumo.insumos'))
        except ValueError as e:
            flash(str(e), "danger")
    elif request.method == 'POST':
        flash("Por favor, corrige los errores en el formulario.", "danger")
    return render_template('insumo/editar_insumo.html', form=form, insumo_id=insumo_id)