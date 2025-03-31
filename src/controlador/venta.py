from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from bd import bd
from servicio.inventario import InventarioServicio
from servicio.venta import VentaServicio
from formularios.venta import VentaForm
from flask_login import login_required, current_user
from flask_principal import Permission, RoleNeed

controlador = Blueprint('venta', __name__)

admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

@controlador.route('/ventas/mostrador', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def mostrador():
    busqueda = request.args.get('busqueda', None)
    venta_servicio = VentaServicio(bd)
    carrito, total, _ = venta_servicio.obtener_carrito(session)
    mostrador = venta_servicio.obtener_mostrador(busqueda)
    session['comprador'] = None
    return render_template('venta/mostrador.html', mostrador=mostrador, carrito=carrito, total=total, busqueda=busqueda)

@controlador.route('/ventas/carrito/agregar', methods=['POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def agregar_galleta():
    try:
        venta_servicio = VentaServicio(bd)
        venta_servicio.agregar_galleta(request.form, session)
        flash("Galleta agregada al carrito", "success")
        return redirect(url_for('principal.venta.ver_carrito'))
    except Exception as e:
        print(e.__class__.__name__)
        if hasattr(e, 'message'):
            flash(e.message, "danger")
        elif hasattr(e, 'description'):
            flash(e.description, "danger")
        else:
            flash(str(e), "danger")
        return redirect(request.referrer)
    
@controlador.route('/ventas/carrito/modificar', methods=['POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def modificar_cantidad():
    try:
        venta_servicio = VentaServicio(bd)
        carrito = venta_servicio.modificar_cantidad(request.form, session)
        flash("Cantidad actualizada", "success")
        return redirect(url_for('principal.venta.ver_carrito'))
    except Exception as e:
        flash("Error actualizando la cantidad: " + str(e), "danger")
        return redirect(url_for('principal.venta.ver_carrito'))
    
@controlador.route('/ventas/carrito/eliminar', methods=['POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def eliminar_galleta():
    try:
        venta_servicio = VentaServicio(bd)
        carrito = venta_servicio.eliminar_galleta(request.form, session)
        flash("Galleta removida del carrito", "success")
        if len(carrito) != 0:
            return redirect(url_for('principal.venta.ver_carrito'))
        else:
            return redirect(url_for('principal.venta.mostrador'))
    except Exception as e:
        flash("Error al eliminar galleta: " + str(e), "danger")
        return redirect(url_for('principal.venta.ver_carrito'))

@controlador.route('/ventas/carrito', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def ver_carrito():
    venta_formulario = VentaForm()
    venta_servicio = VentaServicio(bd)
    carrito, total, buscar_comprador = venta_servicio.obtener_carrito(session)
    try:
        session['carrito'] = carrito
        session['precio_total'] = total
        session.modified = True
        return render_template('venta/carrito.html', carrito=carrito, total=total, form=venta_formulario)
    except Exception as e:
        flash("Error al obtener el carrito: " + str(e), "danger")
        return redirect(url_for('principal.venta.mostrador'))

@controlador.route('/ventas/carrito/vaciar', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def vaciar_carrito():
    session.pop('carrito', None)
    session.pop('cantidad_total', None)
    session.pop('precio_total', None)
    flash("Carrito vaciado", "info")
    return redirect(url_for('principal.venta.mostrador'))

@controlador.route('/ventas/comprador', methods=['POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def buscar_comprador():
    form = VentaForm(request.form)
    venta_servicio = VentaServicio(bd)
    carrito, total, comprador = venta_servicio.obtener_carrito(session)
    if form.validate():
        comprador = venta_servicio.buscar_comprador(form)
        if comprador:
            session['comprador'] = comprador.id
            session.modified = True
            flash("Comprador encontrado", "success")
        else:
            session['comprador'] = None
            session.modified = True
            form.email_comprador.errors.append("Comprador no encontrado")
    return render_template('venta/carrito.html', carrito=carrito, total=total, form=form)

@controlador.route('/ventas/cerrar', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def cerrar_venta():
    try:
        venta_servicio = VentaServicio(bd)
        venta_servicio.cerrar_venta(session, current_user)
        flash("Venta cerrada con éxito", "success")
    except Exception as e:
        print(e.__class__.__name__)
        if hasattr(e, 'message'):
            flash(e.message, "danger")
        elif hasattr(e, 'description'):
            flash(e.description, "danger")
        else:
            flash(str(e), "danger")
    return redirect(url_for('principal.venta.mostrador'))