from modelo.galleta import Galleta
from modelo.usuario import Usuario
from modelo.rol import Rol
from modelo.venta import Venta
from modelo.venta_detalle import VentaDetalle
from modelo.galleta_inventario import GalletaInventario
from modelo.medida import Medida
from sqlalchemy import func
import re
import math
from datetime import datetime

class VentaServicio:
    
    def __init__(self, bd):
        self.bd = bd
        
    def buscar_comprador(self, form):
        email = form.email_comprador.data
        return self.bd.session.query(Usuario).filter_by(email=email).first()
        
    def obtener_galleta(self, id):
        return self.bd.session.query(Galleta).get(id)
    
    def obtener_inventario(self, galleta_id):
        return self.bd.session.query(GalletaInventario).filter_by(galleta_id=galleta_id).first()
    
    def obtener_menu(self, busqueda=None):
        query = (
            self.bd.session
            .query(
                Galleta.id,
                Galleta.nombre,
                func.sum(GalletaInventario.cantidad).label("cantidad_total"),
                func.min(Galleta.precio).label("precio"),
                Galleta.imagen,
                Medida.nombre
            )
            .join(Galleta, Galleta.id == GalletaInventario.galleta_id)
            .join(Medida, GalletaInventario.medida_id == Medida.id)
            .filter(GalletaInventario.fecha_expiracion > datetime.now())
            .filter(GalletaInventario.cantidad > 0)
        )
        
        if busqueda:
            # Búsqueda insensible a mayúsculas
            query = query.filter(Galleta.nombre.ilike(f"%{busqueda}%"))
        query = query.group_by(Galleta.id, Galleta.nombre, Medida.nombre)
        query = query.order_by(func.sum(GalletaInventario.cantidad).desc())
        resultados = query.all()
        galletas = [
            {
                "galleta_id": galleta_id,
                "galleta": nombre,
                "cantidad": float(cantidad_total),
                "precio": precio,
                "imagen": imagen,
                "medida": medida
            }
            for galleta_id, nombre, cantidad_total, precio, imagen, medida in resultados
        ]
        return galletas
    
    def obtener_mostrador(self, busqueda=None):
        query = (
            self.bd.session
            .query(
                Galleta.id,
                Galleta.nombre,
                func.sum(GalletaInventario.cantidad).label("cantidad_total"),
                func.min(Galleta.precio).label("precio"),
                Galleta.imagen,
                Medida.nombre
            )
            .join(Galleta, Galleta.id == GalletaInventario.galleta_id)
            .join(Medida, GalletaInventario.medida_id == Medida.id)
            .filter(GalletaInventario.fecha_expiracion > datetime.now())
        )
        
        if busqueda:
            # Búsqueda insensible a mayúsculas
            query = query.filter(Galleta.nombre.ilike(f"%{busqueda}%"))
        
        query = query.group_by(Galleta.id, Galleta.nombre, Medida.nombre)
        query = query.order_by(func.sum(GalletaInventario.cantidad).desc())
        resultados = query.all()
        
        galletas = [
            {
                "galleta_id": galleta_id,
                "galleta": nombre,
                "cantidad": float(cantidad_total),
                "precio": precio,
                "imagen": imagen,
                "medida": medida
            }
            for galleta_id, nombre, cantidad_total, precio, imagen, medida in resultados
        ]
        return galletas

        
    def cerrar_venta(self, session, form, current_user):
        horarios = {
            'Lunes': [8, 20],
            'Martes': [8, 20],
            'Miércoles': [8, 20],
            'Jueves': [8, 20],
            'Viernes': [8, 20],
            'Sábado': [8, 20],
            'Domingo': [8, 16]
        }
        
        carrito = session.get('carrito', {})
        total = float(math.ceil(session.get('total', 0)))
        
        venta = Venta()
        venta.fecha = datetime.now()
        venta.fecha_entrega = form.fecha_entrega.data if current_user.rol.nombre == 'COMPRADOR' else datetime.now()
        venta.pagado = False if current_user.rol.nombre == 'COMPRADOR' else True
        venta.comprador_id = current_user.id if current_user.rol.nombre == 'COMPRADOR' else session.get('comprador', None)
        venta.vendedor_id = None if current_user.rol.nombre == 'COMPRADOR' else current_user.id
        venta.total = total
        
        self.bd.session.add(venta)
        self.bd.session.flush()  # Force insert so that venta.id is generated
        
        for key, item in carrito.items():
            detalle = VentaDetalle()
            galleta = self.bd.session.query(Galleta).get(item['galleta_id'])
            
            if galleta is None:
                raise ValueError("Galleta no encontrada")
            
            detalle.venta_id = venta.id
            detalle.galleta_id = galleta.id
            detalle.presentacion = item['presentacion']
            detalle.cantidad = item['cantidad']
            detalle.medida_id = item['medida_id']
            detalle.precio_unitario = item['precio']
            detalle.precio_total = item['subtotal']
            
            inventario = self.bd.session.query(GalletaInventario).filter_by(galleta_id=galleta.id).first()
            if inventario is None:
                raise ValueError("Inventario no encontrado")
            if inventario.cantidad < item['peso']:
                raise ValueError("No hay suficiente inventario")
            inventario.cantidad -= item['peso']
            self.bd.session.add(detalle)
            self.bd.session.add(inventario)
        self.bd.session.commit()
        
        session.pop('carrito', None)
        session.pop('total', None)
        session.pop('cantidad_total', None)
        session.pop('comprador', None)
        session.modified = True
    
    def agregar_galleta(self, form, session):
        print("Formulario recibido:", form)
        presentacion = form.get('presentacion', "0")
        galleta_id = int(form.get('galleta_id'))
        medida_id = int(form.get('medida_id'))
        
        presentaciones = {
            "1 pz": 0.05,
            "2 pz": 0.1,
            "5 pz": 0.25,
            "500 g": 0.5,
            "700 g": 0.7,
            "1 kg": 1
        }
        
        peso = presentaciones.get(presentacion)
        unidad = re.sub(r'^[0-9\s]+', '', presentacion).strip()
        if "pz" in presentacion.lower():
            cuenta = int(re.sub(r'[^0-9]', '', presentacion))
        elif "g" in presentacion.lower():
            cuenta = int(re.sub(r'[^0-9]', '', presentacion)) / 1000
        else:
            cuenta = 1
        
        galleta = self.obtener_galleta(galleta_id)
        if not galleta:
            raise ValueError("Galleta no encontrada")
        
        inventario = self.obtener_inventario(galleta_id)
        if not inventario:
            raise ValueError("Inventario no encontrado")
        if inventario.cantidad <= 0:
            raise ValueError("Inventario no disponible")
        if inventario.cantidad < peso:
            raise ValueError("No hay suficiente inventario")
        
        key_item = f"{galleta.nombre} {presentacion}"
        # Calcular precio unitario: (valor de presentación / 0.05) * precio de la galleta
        precio_unitario = float(math.ceil((peso / 0.05) * galleta.precio))
        
        item = {
            'galleta_id': galleta_id,
            'nombre': galleta.nombre,
            'presentacion': presentacion,
            'unidad': unidad,
            'cuenta': cuenta,
            'peso': peso,  # peso correspondiente a una unidad de esta presentación
            'precio': precio_unitario,
            'medida_id': medida_id,
            'cantidad': 1,
            'subtotal': precio_unitario,  # subtotal = precio_unitario * cantidad (inicialmente 1)
            'imagen': galleta.imagen,
        }
        
        total_peso_actual = sum(
            itm['peso'] for itm in session.get('carrito', {}).values() if itm['galleta_id'] == galleta_id
        )
        nueva_peso_total = total_peso_actual + peso
        if round(nueva_peso_total, 2) > inventario.cantidad:
            raise ValueError("No hay suficiente inventario para agregar este artículo")
        
        session.modified = True
        if 'carrito' in session:
            if key_item in session['carrito']:
                current_item = session['carrito'][key_item]
                nueva_cantidad = current_item['cantidad'] + 1
                current_item['cantidad'] = nueva_cantidad
                current_item['peso'] += peso
                current_item['subtotal'] = current_item['cantidad'] * precio_unitario
                session['total'] = math.ceil(sum(itm['subtotal'] for itm in session['carrito'].values()))
                session['cantidad_total'] = sum(itm['cantidad'] for itm in session['carrito'].values())
            else:
                session['carrito'][key_item] = item
                session['total'] = math.ceil(sum(itm['subtotal'] for itm in session['carrito'].values()))
                session['cantidad_total'] = sum(itm['cantidad'] for itm in session['carrito'].values())
            return session['carrito']
        else:
            session['carrito'] = {key_item: item}
            session['total'] = item['subtotal']
            session['cantidad_total'] = 1
            session['comprador'] = None
            session.modified = True
            return session['carrito']
        
    def modificar_cantidad(self, form, session):
        key_item = form.get('key_item')
        try:
            nueva_cantidad = int(form.get('cantidad'))
        except ValueError:
            raise ValueError("La cantidad debe ser un número entero")
        
        if 'carrito' not in session or key_item not in session['carrito']:
            raise ValueError("Item no encontrado en el carrito")
        
        carrito = session['carrito']
        item = carrito[key_item]
        # Recuperar el inventario para la galleta
        inv = self.obtener_inventario(item['galleta_id'])
        if not inv:
            raise ValueError("Inventario no encontrado para este artículo")
        
        # Primero, calcular el peso unitario (el mismo que se usó al agregar el item)
        if item['cantidad'] <= 0:
            raise ValueError("Cantidad actual inválida")
        unit_weight = item['peso'] / item['cantidad']
        
        # Calcular el nuevo peso para este item
        nuevo_peso_item = nueva_cantidad * unit_weight
        
        # Calcular el peso total de esta galleta en el carrito, excluyendo el item a modificar
        peso_otros = sum(itm['peso'] for k, itm in carrito.items() 
                        if itm['galleta_id'] == item['galleta_id'] and k != key_item)
        
        nuevo_total_peso = peso_otros + nuevo_peso_item
        if round(nuevo_total_peso, 2) > inv.cantidad:
            raise ValueError("No hay suficiente inventario para modificar este artículo")
        
        if nueva_cantidad <= 0:
            del carrito[key_item]
        else:
            item['cantidad'] = nueva_cantidad
            item['peso'] = nuevo_peso_item
            item['subtotal'] = nueva_cantidad * item['precio']  # precio es el precio unitario
        
        # Actualizar totales globales
        session['total'] = math.ceil(sum(itm['subtotal'] for itm in carrito.values()))
        session['cantidad_total'] = sum(itm['cantidad'] for itm in carrito.values())
        session.modified = True
        return carrito
    
    def eliminar_galleta(self, form, session):
        key_item = form.get('key_item')
        if 'carrito' in session and key_item in session['carrito']:
            item = session['carrito'][key_item]
            if item['cantidad'] > 1:
                item['cantidad'] -= 1
                # Actualizar opcionalmente el peso acumulado (restando el peso unitario)
                unit_weight = item['peso'] / (item['cantidad'] + 1)
                item['peso'] -= unit_weight
                item['subtotal'] = item['cantidad'] * item['precio']
            else:
                del session['carrito'][key_item]
            # Actualizar totales globales
            session['total'] = math.ceil(sum(itm['subtotal'] for itm in session['carrito'].values()))
            session['cantidad_total'] = sum(itm['cantidad'] for itm in session['carrito'].values())
            session.modified = True
            return session['carrito']
        else:
            raise ValueError("Item not found in cart")
    
    def obtener_carrito(self, session):
        carrito = session.get('carrito', {})
        total = float(math.ceil(session.get('total', 0)))
        comprador = session.get('comprador', None)
        print("Carrito:", carrito)
        print("Total:", total)
        print("Comprador:", comprador)
        if not carrito:
            return {}, 0, None
        return carrito, total, comprador