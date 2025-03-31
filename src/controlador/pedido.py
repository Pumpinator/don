from flask import Blueprint, render_template, request, redirect, url_for, session, flash, abort
from bd import bd
from servicio.venta import VentaServicio
from formularios.venta import VentaForm
from flask_login import login_required, current_user
from flask_principal import Permission, RoleNeed

controlador = Blueprint('pedido', __name__)

comprador_permission = Permission(RoleNeed('COMPRADOR'))

@controlador.before_request
def before_request():
    if current_user.is_authenticated:
        if current_user.rol.nombre == 'TRABAJADOR' or current_user.rol == 'ADMIN':
            abort(403)
        else:
            pass
    else:
        session['comprador'] = None
    session.modified = True

@controlador.route('/menu', methods=['GET'])
def menu():
    busqueda = request.args.get('busqueda', '')
    venta_servicio = VentaServicio(bd)
    carrito, total, _ = venta_servicio.obtener_carrito(session)
    galletas = venta_servicio.obtener_menu(busqueda)
    return render_template('venta/menu.html', galletas=galletas, carrito=carrito, total=total, busqueda=busqueda)

@controlador.route('/carrito', methods=['GET'])
def ver_carrito():
    venta_formulario = VentaForm()
    venta_servicio = VentaServicio(bd)
    carrito, total, buscar_comprador = venta_servicio.obtener_carrito(session)
    try:
        session['carrito'] = carrito
        session['precio_total'] = total
        session.modified = True
        return render_template('venta/pedido.html', carrito=carrito, total=total, form=venta_formulario)
    except Exception as e:
        flash("Error al obtener el carrito: " + str(e), "danger")
        return redirect(url_for('principal.pedido.menu'))

@controlador.route('/carrito/agregar', methods=['POST'])
def agregar_galleta():
    try:
        venta_servicio = VentaServicio(bd)
        venta_servicio.agregar_galleta(request.form, session)
        flash("Galleta agregada al carrito", "success")
        return redirect(url_for('principal.pedido.ver_carrito'))
    except Exception as e:
        print(e.__class__.__name__)
        if hasattr(e, 'message'):
            flash(e.message, "danger")
        elif hasattr(e, 'description'):
            flash(e.description, "danger")
        else:
            flash(str(e), "danger")
        return redirect(request.referrer)
    
@controlador.route('/carrito/modificar', methods=['POST'])
def modificar_cantidad():
    try:
        venta_servicio = VentaServicio(bd)
        carrito = venta_servicio.modificar_cantidad(request.form, session)
        flash("Cantidad actualizada", "success")
        return redirect(url_for('principal.pedido.ver_carrito'))
    except Exception as e:
        flash("Error actualizando la cantidad: " + str(e), "danger")
        return redirect(url_for('principal.pedido.ver_carrito'))
    
@controlador.route('/carrito/eliminar', methods=['POST'])
def eliminar_galleta():
    try:
        venta_servicio = VentaServicio(bd)
        carrito = venta_servicio.eliminar_galleta(request.form, session)
        flash("Galleta removida del carrito", "success")
        if len(carrito) != 0:
            return redirect(url_for('principal.pedido.ver_carrito'))
        else:
            return redirect(url_for('principal.pedido.menu'))
    except Exception as e:
        flash("Error al eliminar galleta: " + str(e), "danger")
        return redirect(url_for('principal.pedido.ver_carrito'))

@controlador.route('/carrito/vaciar', methods=['GET'])
@login_required
def vaciar_carrito():
    session.pop('carrito', None)
    session.pop('cantidad_total', None)
    session.pop('precio_total', None)
    flash("Carrito vaciado", "info")
    return redirect(url_for('principal.pedido.menu'))


@controlador.route('/carrito/pagar', methods=['POST'])
@login_required
@comprador_permission.require(http_exception=403)
def cerrar_venta():
    try:
        venta_servicio = VentaServicio(bd)
        form = VentaForm(request.form)
        venta_servicio.cerrar_venta(session, form, current_user)
        flash("Venta cerrada con éxito", "success")
    except Exception as e:
        print(e.__class__.__name__)
        if hasattr(e, 'message'):
            flash(e.message, "danger")
        elif hasattr(e, 'description'):
            flash(e.description, "danger")
        else:
            flash(str(e), "danger")
    return redirect(url_for('principal.pedido.menu'))