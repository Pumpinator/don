from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from flask_principal import Permission, RoleNeed
from servicio.proveedor import ProveedorServicio
from bd import bd

controlador = Blueprint('proveedor', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

@controlador.route('/proveedores')
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def proveedores():
    servicio = ProveedorServicio(bd)
    return render_template('proveedor/proveedores.html', proveedores=servicio.obtener_proveedores())

@controlador.route('/proveedor/crear', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def crear_proveedor():
    if request.method == 'POST':
        try:
            servicio = ProveedorServicio(bd)
            servicio.crear_proveedor(
                nombre=request.form['nombre'],
                contacto=request.form['contacto']
            )
            flash("Proveedor creado exitosamente", "success")
            return redirect(url_for('principal.proveedor.proveedores'))
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for('principal.proveedor.crear_proveedor'))
    
    return render_template('proveedor/crear_proveedor.html')

@controlador.route('/proveedor/editar/<int:proveedor_id>', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def editar_proveedor(proveedor_id):
    servicio = ProveedorServicio(bd)
    proveedor = servicio.obtener_proveedor_por_id(proveedor_id)
    
    if request.method == 'POST':
        try:
            servicio.editar_proveedor(
                proveedor_id=proveedor_id,
                nombre=request.form['nombre'],
                contacto=request.form['contacto']
            )
            flash("Proveedor actualizado correctamente", "success")
            return redirect(url_for('principal.proveedor.proveedores'))
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
    
    return render_template('proveedor/editar_proveedor.html', proveedor=proveedor)

@controlador.route('/proveedor/eliminar/<int:proveedor_id>', methods=['POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def eliminar_proveedor(proveedor_id):
    try:
        servicio = ProveedorServicio(bd)
        servicio.eliminar_proveedor(proveedor_id)
        flash("Proveedor eliminado exitosamente", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('principal.proveedor.proveedores'))

@controlador.route('/proveedor/detalles/<int:proveedor_id>', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def detalles_proveedor(proveedor_id):
    try:
        servicio = ProveedorServicio(bd)
        proveedor = servicio.obtener_proveedor_por_id(proveedor_id)
        return render_template('proveedor/detalles_proveedor.html', proveedor=proveedor)
    except Exception as e:
        flash(f"Error al cargar los detalles del proveedor: {str(e)}", "danger")
        return redirect(url_for('principal.proveedor.proveedores'))