from modelo.galleta import Galleta
from modelo.usuario import Usuario
from modelo.rol import Rol
from modelo.venta import Venta
from modelo.venta_detalle import VentaDetalle
from modelo.galleta_inventario import GalletaInventario
from modelo.medida import Medida
from sqlalchemy import func, case
from sqlalchemy.orm import joinedload
import re
import math
from datetime import datetime

class VentaServicio:
    
    def __init__(self, bd):
        self.bd = bd
        
    def validar_comprador(self, form):
        email = form.email_comprador.data
        return self.bd.session.query(Usuario).filter_by(email=email).first()
        
    def obtener_galleta(self, id):
        return self.bd.session.query(Galleta).get(id)
    
    def obtener_inventario(self, galleta_id):
        now = datetime.now()
        conversion = case(
            (GalletaInventario.medida_id == 3, GalletaInventario.cantidad * 0.05),
            else_=GalletaInventario.cantidad
        )
        resultado = (
            self.bd.session.query(func.sum(conversion))
            .filter(
                GalletaInventario.galleta_id == galleta_id,
                GalletaInventario.fecha_expiracion > now,
                GalletaInventario.cantidad > 0
            )
            .group_by(GalletaInventario.galleta_id)
            .scalar()
        )
        return round(resultado, 2) if resultado is not None else 0
    
    def obtener_venta(self, venta_id, session):
        venta = (
            self.bd.session.query(Venta)
            .options(joinedload(Venta.comprador))
            .filter(Venta.id == venta_id)
            .first()
        )
        if not venta:
            raise ValueError("Venta no encontrada")
        
        # Query the order details for this sale
        detalles_query = (
            self.bd.session.query(VentaDetalle)
            .options(joinedload(VentaDetalle.galleta))
            .options(joinedload(VentaDetalle.medida))
            .filter(VentaDetalle.venta_id == venta_id)
        )
        
        detalles = [self._construir_detalle_item(
            detalle.galleta,
            detalle.presentacion,
            int(detalle.cantidad),
            detalle.medida,
            detalle.precio_unitario,
            detalle.precio_total)
        for detalle in detalles_query.all()]

        if not venta.pagado:
            carrito = self.poblar_carrito_desde_venta({'detalles': detalles})
            session['carrito'] = carrito
            session['total'] = venta.total
            session['venta_id'] = venta.id
            session['email_comprador'] = venta.comprador.email
            session.modified = True
        
        return {
            "venta_id": venta.id,
            "comprador": venta.comprador.email,
            "fecha": venta.fecha.strftime('%d/%m/%Y'),
            "fecha_entrega": venta.fecha_entrega.strftime('%d/%m/%Y') if venta.fecha_entrega else None,
            "pagado": venta.pagado,
            "total": venta.total,
            "detalles": detalles
        }
        
    def poblar_carrito_desde_venta(self, venta_data):
        carrito = {}
        for detalle in venta_data['detalles']:
            key = f"{detalle['nombre']} {detalle['presentacion']}"
            carrito[key] = detalle
        return carrito
    
    def obtener_ventas(self, busqueda=None, pagado=True):
        query = (
            self.bd.session.query(Venta)
            .options(joinedload(Venta.comprador))
            .filter(Venta.pagado == pagado)
        )
        if busqueda:
            query = query.filter(Venta.fecha.ilike(f"%{busqueda}%"))
            
        query = query.order_by(Venta.fecha.desc())
        resultados = query.all()
        ventas = [
            {
                "id": venta.id,
                "fecha": venta.fecha.strftime('%d/%m/%Y'),
                "fecha_entrega": venta.fecha_entrega.strftime('%d/%m/%Y') if venta.fecha_entrega else None,
                "pagado": venta.pagado,
                "total": venta.total,
                "comprador": venta.comprador   # Now comprador attributes are loaded via joinedload
            }
            for venta in resultados
        ]
        for venta in ventas:
            detalles = self.bd.session.query(
                VentaDetalle.galleta,
                VentaDetalle.presentacion,
                VentaDetalle.cantidad,
                VentaDetalle.medida,
                VentaDetalle.precio_unitario,
                VentaDetalle.precio_total
            ).join(Galleta, Galleta.id == VentaDetalle.galleta_id).join(Medida, Medida.id == VentaDetalle.medida_id).filter(VentaDetalle.venta_id == venta['id']).all()
            
            venta['detalles'] = [
                {
                    "galleta": galleta,
                    "presentacion": presentacion,
                    "cantidad": cantidad,
                    "medida": medida,
                    "precio_unitario": precio_unitario,
                    "precio_total": precio_total
                }
                for galleta, presentacion, cantidad, medida, precio_unitario, precio_total in detalles
            ]
        return ventas
    
    def obtener_menu(self, busqueda=None):
        query = (
            self.bd.session.query(
                Galleta.id,
                Galleta.nombre,
                func.sum(GalletaInventario.cantidad).label("cantidad"),
                func.min(Galleta.precio).label("precio"),
                Galleta.imagen,
                func.min(Medida.nombre).label("medida")  # Se usa MIN para obtener la medida
            )
            .join(Galleta, Galleta.id == GalletaInventario.galleta_id)
            .join(Medida, GalletaInventario.medida_id == Medida.id)
        )
        
        if busqueda:
            query = query.filter(Galleta.nombre.ilike(f"%{busqueda}%"))
        
        query = query.group_by(Galleta.id, Galleta.nombre, Galleta.imagen)
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
            self.bd.session.query(
                Galleta.id,
                Galleta.nombre,
                func.sum(GalletaInventario.cantidad).label("cantidad"),
                func.min(Galleta.precio).label("precio"),
                Galleta.imagen,
                func.min(Medida.nombre).label("medida")  # Se usa MIN para obtener la medida
            )
            .join(Galleta, Galleta.id == GalletaInventario.galleta_id)
            .join(Medida, GalletaInventario.medida_id == Medida.id)
        )
        
        if busqueda:
            query = query.filter(Galleta.nombre.ilike(f"%{busqueda}%"))
        
        query = query.group_by(Galleta.id, Galleta.nombre, Galleta.imagen)
        query = query.order_by(func.sum(GalletaInventario.cantidad).desc())
        resultados = query.all()
        
        galletas = [
            {
                "galleta_id": galleta_id,
                "galleta": nombre,
                "cantidad": float(cantidad),
                "precio": precio,
                "imagen": imagen,
                "medida": medida
            }
            for galleta_id, nombre, cantidad, precio, imagen, medida in resultados
        ]
        return galletas
            
    def cerrar_pedido(self, session, form, current_user):
        carrito = session.get('carrito', {})
        total = float(math.ceil(session.get('total', 0)))
        
        venta = Venta()
        venta.fecha = datetime.now()
        venta.fecha_entrega = form.fecha_entrega.data
        venta.pagado = False
        venta.comprador_id = current_user.id
        venta.vendedor_id = None
        venta.total = total + 50
        
        self.bd.session.add(venta)
        self.bd.session.flush()
        
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
            
            # No se debe restar inventario en el pedido, solo se conservan los detalles.
            self.bd.session.add(detalle)
            
        session.pop('carrito', None)
        session.pop('total', None)
        session.pop('cantidad_total', None)
        session.pop('email_comprador', None)
        
        self.bd.session.commit()
        session.modified = True
        
    def cerrar_venta(self, session, current_user):
        carrito = session.get('carrito', {})
        total = float(math.ceil(session.get('total', 0)))
        venta_id = session.get('venta_id', None)
        email_comprador = session.get('email_comprador', None)

        if venta_id:
            venta = self.bd.session.query(Venta).get(venta_id)
            self.bd.session.query(VentaDetalle).filter(VentaDetalle.venta_id == venta.id).delete(synchronize_session=False)
        else:
            venta = Venta()
            comprador = self.bd.session.query(Usuario).filter_by(email=email_comprador).first()
            venta.comprador_id = comprador.id if comprador else None
            venta.fecha = datetime.now()

        venta.fecha_entrega = datetime.now()
        venta.total = total
        venta.pagado = True
        venta.vendedor_id = current_user.id

        self.bd.session.add(venta)
        self.bd.session.flush()  # Para tener el id de la venta

        # Crear un diccionario virtual para evitar volver a consultar la BD tras modificar
        virtual_inventory = {}

        for key, item in carrito.items():
            detalle = VentaDetalle()
            galleta = self.bd.session.query(Galleta).get(item['galleta_id'])
            if not galleta:
                raise ValueError("Galleta no encontrada")

            detalle.venta_id = venta.id
            detalle.galleta_id = galleta.id
            detalle.presentacion = item['presentacion']
            detalle.cantidad = item['cantidad']
            detalle.medida_id = item['medida_id']
            detalle.precio_unitario = item['precio']
            detalle.precio_total = item['subtotal']

            # Si aún no se tiene el inventario virtual para esta galleta, se consulta
            if galleta.id not in virtual_inventory:
                virtual_inventory[galleta.id] = self.obtener_inventario(galleta.id)
            
            requerido = item['peso']
            if virtual_inventory[galleta.id] < requerido:
                raise ValueError("No hay suficiente inventario")
            
            # Descontar el requerido del inventario virtual
            virtual_inventory[galleta.id] -= requerido

            # Ahora, proceder a descontar de los registros reales de inventario
            now = datetime.now()
            inventarios = (
                self.bd.session.query(GalletaInventario)
                .filter(
                    GalletaInventario.galleta_id == galleta.id,
                    GalletaInventario.fecha_expiracion > now,
                    GalletaInventario.cantidad > 0  # se consideran solo registros activos
                )
                .order_by(GalletaInventario.fecha_expiracion.asc())
                .all()
            )
            restante = requerido
            for inventario in inventarios:
                if restante <= 0:
                    break
                if inventario.medida_id == 3:
                    # Cantidad en piezas: convertir a kg
                    disponible_kg = inventario.cantidad * 0.05
                    if disponible_kg >= restante:
                        piezas_restantes = (disponible_kg - restante) / 0.05
                        inventario.cantidad = piezas_restantes
                        restante = 0
                        break
                    else:
                        restante -= disponible_kg
                        inventario.cantidad = 0
                else:
                    # Registro en kg
                    disponible = inventario.cantidad
                    if disponible >= restante:
                        inventario.cantidad = disponible - restante
                        restante = 0
                        break
                    else:
                        restante -= disponible
                        inventario.cantidad = 0
            self.bd.session.add(detalle)
        self.bd.session.commit()
        self.vaciar_carrito(session)
    
    def agregar_galleta(self, form, session):
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

        galleta = self.obtener_galleta(galleta_id)
        if not galleta:
            raise ValueError("Galleta no encontrada")
        
        inventario_total = self.obtener_inventario(galleta_id)
        if inventario_total <= 0:
            raise ValueError("Inventario no disponible")
        if inventario_total < peso:
            raise ValueError("No hay suficiente inventario")
        
        key_item = f"{galleta.nombre} {presentacion}"
        precio_unitario = float(math.ceil((peso / 0.05) * galleta.precio))
        
        medida_obj = self.bd.session.query(Medida).get(medida_id)
        item = self._construir_detalle_item(galleta, presentacion, 1, medida_obj, precio_unitario, precio_unitario)
        
        total_peso_actual = sum(
            itm['peso'] for itm in session.get('carrito', {}).values() if itm['galleta_id'] == galleta_id
        )
        nueva_peso_total = total_peso_actual + peso
        if round(nueva_peso_total, 2) > inventario_total:
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
        else:
            session['carrito'] = {key_item: item}
            session['total'] = item['subtotal']
            session['cantidad_total'] = 1
            session['email_comprador'] = None
            session.modified = True
        if session.get('venta_id'):
            session['total'] = session['total'] + 50
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
        inventario_total = self.obtener_inventario(item['galleta_id'])
        if inventario_total <= 0:
            raise ValueError("Inventario no disponible")
        # Si la cantidad es 0, eliminar el item del carrito
        if nueva_cantidad == 0:
            del carrito[key_item]
            session['cantidad_total'] = sum(itm['cantidad'] for itm in carrito.values())
            session['total'] = math.ceil(sum(itm['subtotal'] for itm in carrito.values()))
            session.modified = True
            return carrito
        
        # Calcular el peso unitario de este item
        unit_weight = item['peso'] / item['cantidad']
        
        # Calcular el nuevo peso para este item
        nuevo_peso_item = nueva_cantidad * unit_weight
        
        # Calcular el peso total de esta galleta en el carrito, excluyendo el item a modificar
        peso_otros = sum(itm['peso'] for k, itm in carrito.items() 
                        if itm['galleta_id'] == item['galleta_id'] and k != key_item)
        
        nuevo_total_peso = peso_otros + nuevo_peso_item
        if round(nuevo_total_peso, 2) > inventario_total:
            raise ValueError("No hay suficiente inventario para modificar este artículo")
        
        if nueva_cantidad <= 0:
            del carrito[key_item]
        else:
            item['cantidad'] = nueva_cantidad
            item['peso'] = nuevo_peso_item
            item['subtotal'] = nueva_cantidad * item['precio']  # precio es el precio unitario
        
        # Actualizar totales globales
        session['total'] = math.ceil(sum(itm['subtotal'] for itm in carrito.values()))
        if session.get('venta_id'):
            session['total'] = session['total'] + 50
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
            if session.get('venta_id'):
                session['total'] = session['total'] + 50
            session['cantidad_total'] = sum(itm['cantidad'] for itm in session['carrito'].values())
            session.modified = True
            return session['carrito']
        else:
            raise ValueError("Item not found in cart")
        
    def vaciar_carrito(self, session):
        session.pop('carrito', None)
        session.pop('cantidad_total', None)
        session.pop('precio_total', None)
        session.pop('email_comprador', None)
        session.pop('venta_id', None)
        session.modified = True
        
    def obtener_carrito(self, session):
        carrito = session.get('carrito', {})
        total = float(math.ceil(session.get('total', 0)))
        email_comprador = session.get('email_comprador', None)
        venta_id = session.get('venta_id', None)
        if not venta_id:
            session['email_comprador'] = None
        return carrito, total, email_comprador, venta_id
    
    def cancelar_pedido(self, session):
        venta_id = session.get('venta_id', None)
        venta = self.bd.session.query(Venta).get(venta_id)
        self.bd.session.query(VentaDetalle).filter(VentaDetalle.venta_id == venta.id).delete(synchronize_session=False)
        self.bd.session.delete(venta)
        self.bd.session.commit()
        self.vaciar_carrito(session)
    
    def _construir_detalle_item(self, galleta, presentacion, cantidad, medida, precio_unitario, precio_total):
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
        return {
            'galleta_id': galleta.id,
            'nombre': galleta.nombre,
            'presentacion': presentacion,
            'unidad': unidad,
            'cuenta': cuenta,
            'peso': peso,  # peso según presentación
            'precio': precio_unitario,  # precio unitario calculado
            'medida_id': medida.id if hasattr(medida, 'id') else medida,
            'cantidad': cantidad,
            'subtotal': precio_total,
            'imagen': galleta.imagen,
        }