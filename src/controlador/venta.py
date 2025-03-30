from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from bd import bd
from servicio.inventario import InventarioServicio
from servicio.venta import VentaServicio
from flask_login import login_required, current_user
from flask_principal import Permission, RoleNeed

controlador = Blueprint('venta', __name__)

trabajador_permission = Permission(RoleNeed('TRABAJADOR'))

@controlador.route('/ventas/mostrador', methods=['GET'])
@login_required
@trabajador_permission.require(http_exception=403)
def mostrador():
    venta_servicio = VentaServicio(bd)
    carrito, total = venta_servicio.obtener_carrito(session)
    mostrador = venta_servicio.obtener_mostrador()
    return render_template('venta/mostrador.html', mostrador=mostrador, carrito=carrito, total=total)

@controlador.route('/ventas/carrito/agregar', methods=['POST'])
@login_required
@trabajador_permission.require(http_exception=403)
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
            flash("Error al agregar galleta: " + str(e), "danger")
        return redirect(request.referrer)
    
@controlador.route('/ventas/carrito/eliminar', methods=['POST'])
@login_required
@trabajador_permission.require(http_exception=403)
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
@trabajador_permission.require(http_exception=403)
def ver_carrito():
    try:
        venta_servicio = VentaServicio(bd)
        carrito, total = venta_servicio.obtener_carrito(session)
        session['carrito'] = carrito
        session['total'] = total
        session.modified = True
        return render_template('venta/carrito.html', carrito=carrito, total=total)
    except Exception as e:
        flash("Error al obtener el carrito: " + str(e), "danger")
        return redirect(url_for('principal.venta.mostrador'))

@controlador.route('/ventas/carrito/vaciar', methods=['GET'])
@login_required
@trabajador_permission.require(http_exception=403)
def vaciar_carrito():
    session.pop('carrito', None)
    session.pop('cantidad_total', None)
    session.pop('precio_total', None)
    flash("Carrito vaciado", "info")
    return redirect(url_for('principal.venta.mostrador'))

@controlador.route('/ventas/cerrar', methods=['POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def cerrar_venta():
    try:
        if 'carrito' not in session or not session['carrito']:
            flash("El carrito está vacío", "warning")
            return redirect(url_for('venta.mostrador'))
        
        # Preparar los detalles de la venta
        detalles = []
        for item in session['carrito'].values():
            detalles.append({
                'galleta_id': item['galleta_id'],
                'cantidad': item['cantidad'],
                'medida_id': item['medida_id']
            })
        data = {
            # Se asume que el usuario actual es el comprador;
            # adapta los IDs según la lógica de tu aplicación.
            'comprador_id': current_user.id,
            'vendedor_id': current_user.id,
            'pagado': False,
            'fecha_entrega': request.form.get('fecha_entrega'),
            'detalles': detalles
        }
        
        # Verificar stock disponible y luego procesar la venta
        # (Se debe implementar lógica de validación en InventarioServicio)
        
        venta_serv = VentaServicio(bd)
        venta_serv.generar_venta(data)
        
        # Reducir el stock de galletas vendido (método a implementar en InventarioServicio)
        inventario_serv = InventarioServicio(bd)
        for det in detalles:
            inventario_serv.reducir_stock(det['galleta_id'], det['cantidad'])
            
        # Vaciar el carrito
        session.pop('carrito', None)
        session.pop('cantidad_total', None)
        session.pop('precio_total', None)
        
        flash("Venta finalizada exitosamente", "success")
        return redirect(url_for('principal.venta.mostrador'))
    except Exception as e:
        print(e)
        flash("Error al finalizar la venta", "danger")
        return redirect(url_for('principal.venta.ver_carrito'))