from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required
from flask_principal import Permission, RoleNeed
from sqlalchemy import text
from modelo.insumo import Insumo
from modelo.medida import Medida
from servicio.compra import CompraServicio
from bd import bd

controlador = Blueprint('compra', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))
admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

@controlador.route('/compras')
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def compras():
    compra_servicio = CompraServicio(bd)
    compras = compra_servicio.obtener_compras()
    return render_template('compra/compras.html', compras=compras)

@controlador.route('/compra/crear', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def crear_compra():
    if request.method == 'POST':
        proveedor_id = request.form['proveedor_id']
        fecha = request.form['fecha']
        total = request.form['total']
        insumos = request.form.getlist('insumo_id[]')
        cantidades = request.form['cantidades']
        precios_unitarios = request.form['precios_unitarios']
        medidas = request.form.getlist('medida_id[]')
        fechas_expiracion = request.form['fechas_expiracion']

        # Convertir listas a cadenas separadas por comas
        insumos_str = ','.join(insumos)
        medidas_str = ','.join(medidas)

        # Llamar al procedimiento almacenado SP_CrearCompra
        query = text("""
            CALL SP_CrearCompra(:proveedor_id, :fecha, :total, :insumos, :cantidades, :precios_unitarios, :medidas, :fechas_expiracion)
        """)
        bd.session.execute(query, {
            'proveedor_id': proveedor_id,
            'fecha': fecha,
            'total': total,
            'insumos': insumos_str,
            'cantidades': cantidades,
            'precios_unitarios': precios_unitarios,
            'medidas': medidas_str,
            'fechas_expiracion': fechas_expiracion
        })
        bd.session.commit()

        return redirect(url_for('principal.compras'))

    # Obtener datos para el formulario
    compra_servicio = CompraServicio(bd)
    proveedores = compra_servicio.obtener_proveedores()
    insumos = bd.session.query(Insumo).all()
    medidas = bd.session.query(Medida).all()
    return render_template('compra/crear_compra.html', proveedores=proveedores, insumos=insumos, medidas=medidas)