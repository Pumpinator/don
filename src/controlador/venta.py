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
    mostrador = venta_servicio.obtener_mostrador()
    return render_template('venta/mostrador.html', mostrador=mostrador)

@controlador.route('/ventas/carrito/agregar', methods=['POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def agregar_galleta():
    try:
        cantidad = float(request.form.get('cantidad', 0))
        galleta_id = int(request.form.get('galleta_id'))
        medida_id = int(request.form.get('medida_id'))
        
        if cantidad > 0 and galleta_id and medida_id:
            inventario_serv = InventarioServicio(bd)
            galleta = inventario_serv.obtener_galleta(galleta_id)
            if not galleta:
                flash("Galleta no encontrada", "danger")
                return redirect(url_for('venta.ventas'))
            
            # Usar el id de galleta como clave en el carrito
            key_item = str(galleta_id)
            item = {
                'galleta_id': galleta_id,
                'nombre': galleta.nombre,
                'cantidad': cantidad,
                'precio': galleta.precio,
                'medida_id': medida_id,
                'precio_total': cantidad * galleta.precio
            }
            session.modified = True
            if 'item' in session:
                if key_item in session['item']:
                    old_qty = session['item'][key_item]['cantidad']
                    new_qty = old_qty + cantidad
                    session['item'][key_item]['cantidad'] = new_qty
                    session['item'][key_item]['precio_total'] = new_qty * galleta.precio
                else:
                    session['item'][key_item] = item
            else:
                session['item'] = { key_item: item }
            
            # Calcular totales
            cantidad_total = sum(item['cantidad'] for item in session['item'].values())
            precio_total = sum(item['precio_total'] for item in session['item'].values())
            session['cantidad_total'] = cantidad_total
            session['precio_total'] = precio_total
            
            flash("Galleta agregada al carrito", "success")
            return redirect(url_for('venta.ventas'))
        else:
            flash("Datos inválidos", "danger")
            return redirect(url_for('venta.ventas'))
    except Exception as e:
        print(e)
        flash("Error al agregar galleta", "danger")
        return redirect(url_for('venta.ventas'))

@login_required
@trabajador_permission.require(http_exception=403)
def agregar_galleta():
    try:
        cantidad = float(request.form.get('cantidad', 0))
        galleta_id = int(request.form.get('galleta_id'))
        medida_id = int(request.form.get('medida_id'))
        
        if cantidad > 0 and galleta_id and medida_id:
            inventario_serv = InventarioServicio(bd)
            galleta = inventario_serv.obtener_galleta(galleta_id)
            if not galleta:
                flash("Galleta no encontrada", "danger")
                return redirect(url_for('venta.ventas'))
            
            # Usar el id de galleta como clave en el carrito
            key_item = str(galleta_id)
            item = {
                'galleta_id': galleta_id,
                'nombre': galleta.nombre,
                'cantidad': cantidad,
                'precio': galleta.precio,
                'medida_id': medida_id,
                'precio_total': cantidad * galleta.precio
            }
            session.modified = True
            if 'item' in session:
                if key_item in session['item']:
                    old_qty = session['item'][key_item]['cantidad']
                    new_qty = old_qty + cantidad
                    session['item'][key_item]['cantidad'] = new_qty
                    session['item'][key_item]['precio_total'] = new_qty * galleta.precio
                else:
                    session['item'][key_item] = item
            else:
                session['item'] = { key_item: item }
            
            # Calcular totales
            cantidad_total = sum(item['cantidad'] for item in session['item'].values())
            precio_total = sum(item['precio_total'] for item in session['item'].values())
            session['cantidad_total'] = cantidad_total
            session['precio_total'] = precio_total
            
            flash("Galleta agregada al carrito", "success")
            return redirect(url_for('venta.ventas'))
        else:
            flash("Datos inválidos", "danger")
            return redirect(url_for('venta.ventas'))
    except Exception as e:
        print(e)
        flash("Error al agregar galleta", "danger")
        return redirect(url_for('venta.ventas'))

@controlador.route('/ventas/carrito', methods=['GET'])
@login_required
@trabajador_permission.require(http_exception=403)
def ver_carrito():
    # Muestra el contenido del carrito de compra
    return render_template('carrito.html')

@controlador.route('/ventas/carrito/vaciar', methods=['GET'])
@login_required
@trabajador_permission.require(http_exception=403)
def vaciar_carrito():
    session.pop('item', None)
    session.pop('cantidad_total', None)
    session.pop('precio_total', None)
    flash("Carrito vaciado", "info")
    return redirect(url_for('venta.ventas'))

@controlador.route('/ventas/carrito/borrar/<int:galleta_id>', methods=['GET'])
@login_required
@trabajador_permission.require(http_exception=403)
def borrar_item(galleta_id):
    session.modified = True
    if 'item' in session and galleta_id in session['item']:
        session['item'].pop(galleta_id)
        if session.get('item'):
            cantidad_total = sum(item['cantidad'] for item in session['item'].values())
            precio_total = sum(item['precio_total'] for item in session['item'].values())
            session['cantidad_total'] = cantidad_total
            session['precio_total'] = precio_total
        else:
            session.pop('cantidad_total', None)
            session.pop('precio_total', None)
    flash("Artículo eliminado", "info")
    return redirect(url_for('venta.ver_carrito'))

@controlador.route('/ventas/cerrar', methods=['POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def cerrar_venta():
    try:
        if 'item' not in session or not session['item']:
            flash("El carrito está vacío", "warning")
            return redirect(url_for('venta.ventas'))
        
        # Preparar los detalles de la venta
        detalles = []
        for item in session['item'].values():
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
        session.pop('item', None)
        session.pop('cantidad_total', None)
        session.pop('precio_total', None)
        
        flash("Venta finalizada exitosamente", "success")
        return redirect(url_for('venta.ventas'))
    except Exception as e:
        print(e)
        flash("Error al finalizar la venta", "danger")
        return redirect(url_for('venta.ver_carrito'))