from flask import Blueprint, render_template, request, redirect, url_for, session, flash, abort
from bd import bd
from servicio.venta import VentaServicio
from formularios.venta import VentaForm
from flask_login import login_required, current_user
from flask_principal import Permission, RoleNeed

controlador = Blueprint('venta', __name__)

admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

@controlador.route('/mostrador', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def mostrador():
    busqueda = request.args.get('busqueda', '')
    venta_servicio = VentaServicio(bd)
    carrito, total, email_comprador, venta_id = venta_servicio.obtener_carrito(session)
    galletas = venta_servicio.obtener_mostrador(busqueda)
    return render_template('venta/mostrador.html', galletas=galletas, carrito=carrito, total=total, busqueda=busqueda)

@controlador.route('/venta/agregar', methods=['POST'])
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
    
@controlador.route('/venta/modificar', methods=['POST'])
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
    
@controlador.route('/venta/eliminar', methods=['POST'])
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




@controlador.route('/venta', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def ver_carrito():
    venta_formulario = VentaForm()
    venta_servicio = VentaServicio(bd)
    carrito, total, email_comprador, venta_id = venta_servicio.obtener_carrito(session)
    return render_template('venta/venta.html', carrito=carrito, total=total, form=venta_formulario, email_comprador=email_comprador, venta_id=venta_id)

@controlador.route('/venta/<int:venta_id>', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def ver_pedido(venta_id):
    venta_servicio = VentaServicio(bd)
    venta = venta_servicio.obtener_venta(venta_id, session)
    carrito, total, email_comprador, venta_id = venta_servicio.obtener_carrito(session)
    venta_formulario = VentaForm(object=venta)
    return render_template('venta/venta.html', form=venta_formulario, carrito=carrito, total=total, email_comprador=email_comprador, venta_id=venta_id, venta=venta)




@controlador.route('/venta/vaciar', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def vaciar_carrito():
    venta_servicio = VentaServicio(bd)
    venta_servicio.vaciar_carrito(session)
    flash("Carrito vaciado", "info")
    return redirect(url_for('principal.venta.mostrador'))


@controlador.route('/pedidos', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def listar_pedidos():
    venta_servicio = VentaServicio(bd)
    pedidos = venta_servicio.obtener_ventas(pagado=False)
    return render_template('venta/pedidos.html', pedidos=pedidos)





@controlador.route('/venta/cancelar', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def cancelar_pedido():
    venta_servicio = VentaServicio(bd)
    venta_servicio.cancelar_pedido(session)
    flash("Pedido cancelado", "info")
    return redirect(url_for('principal.venta.mostrador'))
    





@controlador.route('/comprador', methods=['POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def validar_comprador():
    form = VentaForm(request.form)
    venta_servicio = VentaServicio(bd)
    carrito, total, email_comprador, venta_id = venta_servicio.obtener_carrito(session)
    if form.validate():
        comprador = venta_servicio.validar_comprador(form)
        if comprador:
            session['email_comprador'] = comprador.email
            session.modified = True
            flash("Comprador encontrado", "success")
        else:
            session['email_comprador'] = None
            session.modified = True
            form.email_comprador.errors.append("Comprador no encontrado")
    return render_template('venta/venta.html', carrito=carrito, total=total, form=form)






@controlador.route('/venta/pagar', methods=['GET'])
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