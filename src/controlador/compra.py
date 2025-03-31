from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import login_required
from flask_principal import Permission, RoleNeed
from servicio.compra import CompraServicio
from bd import bd
from servicio.proveedor import ProveedorServicio

controlador = Blueprint('compra', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

# En controlador/compra.py
@controlador.route('/compras')
@login_required
def compras():
    compra_servicio = CompraServicio(bd)
    proveedor_servicio = ProveedorServicio(bd)  # Nuevo
    
    return render_template(
        'compra/compras.html',
        compras=compra_servicio.obtener_compras(),
        proveedores=proveedor_servicio.obtener_proveedores()  # Nuevo
    )

@controlador.route('/compra/crear', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def crear_compra():
    # Obtener los datos de proveedores, insumos y medidas desde el servicio
    servicio = CompraServicio(bd)
    proveedores = servicio.obtener_proveedores()
    insumos = servicio.obtener_insumos()
    medidas = servicio.obtener_medidas()

    if request.method == 'POST':
        try:
            data = {
                'proveedor_id': request.form['proveedor_id'],
                'fecha': request.form['fecha'],
                'total': request.form['total'],
                'insumos': request.form.getlist('insumo_id[]'),
                'cantidades': request.form.getlist('cantidad[]'),
                'precios_unitarios': request.form.getlist('precio[]'),
                'medidas': request.form.getlist('medida_id[]'),
                'fechas_expiracion': request.form.getlist('fecha_expiracion[]')
            }
            
            # Crear la compra utilizando los datos obtenidos
            servicio.crear_compra(data)

            flash("Compra creada exitosamente.", "success")
            return redirect(url_for('principal.compra.compras'))

        except Exception as e:
            flash(f"Ocurrió un error: {str(e)}", "danger")
            return redirect(url_for('principal.compra.compras'))
    
    return render_template(
        'compra/crear_compra.html',
        proveedores=proveedores,
        insumos=insumos,
        medidas=medidas
    )

@controlador.route('/compra/editar/<int:compra_id>', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def editar_compra(compra_id):
    servicio = CompraServicio(bd)
    compra = servicio.obtener_compra(compra_id)
    proveedores = servicio.obtener_proveedores()
    insumos = servicio.obtener_insumos()
    medidas = servicio.obtener_medidas()

    if request.method == 'POST':
        try:
            data = {
                'proveedor_id': request.form['proveedor_id'],
                'fecha': request.form['fecha'],
                'insumos': request.form.getlist('insumo_id[]'),
                'cantidades': request.form.getlist('cantidad[]'),
                'precios_unitarios': request.form.getlist('costo[]'),
                'medidas': request.form.getlist('medida_id[]'),
                'fechas_expiracion': request.form.getlist('fecha_expiracion[]')
            }

            servicio.editar_compra(compra_id, data)
            flash("Compra actualizada exitosamente.", "success")
            return redirect(url_for('principal.compra.compras'))

        except Exception as e:
            flash(f"Ocurrió un error: {str(e)}", "danger")
            return redirect(url_for('principal.compra.compras'))

    return render_template(
        'compra/editar_compra.html',
        compra=compra,
        proveedores=proveedores,
        insumos=insumos,
        medidas=medidas
    )

@controlador.route('/compra/detalles/<int:compra_id>', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def detalles_compra(compra_id):
    servicio = CompraServicio(bd)
    compra = servicio.obtener_compra(compra_id)
    return render_template('compra/detalles_compra.html', compra=compra)
