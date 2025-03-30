from modelo.galleta import Galleta
from modelo.galleta_inventario import GalletaInventario
from modelo.medida import Medida
from sqlalchemy import func
import re
import math

class VentaServicio:
    
    def __init__(self, bd):
        self.bd = bd
        
    def obtener_galleta(self, id):
        return self.bd.session.query(Galleta).get(id)
    
    def obtener_inventario(self, galleta_id):
        return self.bd.session.query(GalletaInventario).filter_by(galleta_id=galleta_id).first()
    
    def obtener_mostrador(self):
        resultados = (
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
            .group_by(Galleta.id, Galleta.nombre, Medida.nombre)
            .all()
        )
        mostrador = [
            {
                "galleta": nombre,
                "galleta_id": galleta_id,
                "cantidad": int(cantidad_total),
                "precio": precio,
                "medida": medida,
                "imagen": imagen,
            }
            for galleta_id, nombre, cantidad_total, precio, imagen, medida in resultados
        ]
        return mostrador
    
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
        unidad = re.sub(r'^[0-9\s]+', '', presentacion).strip()
        if "pz" in presentacion.lower():
            cuenta = int(re.sub(r'[^0-9]', '', presentacion))
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
        print(f"Inventario: {inventario.cantidad}, Peso: {peso}, Cuenta: {cuenta}")
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
        
        session.modified = True
        total_peso_actual = sum(
            itm['peso'] for itm in session.get('carrito', {}).values() if itm['galleta_id'] == galleta_id
        )
        nueva_peso_total = total_peso_actual + peso
        if round(nueva_peso_total, 2) > inventario.cantidad:
            raise ValueError("No hay suficiente inventario para agregar este artículo")
        if 'carrito' in session:
            if key_item in session['carrito']:
                current_item = session['carrito'][key_item]
                nueva_cantidad = current_item['cantidad'] + 1
                current_item['cantidad'] = nueva_cantidad
                current_item['peso'] += peso
                current_item['subtotal'] = current_item['cantidad'] * precio_unitario
            else:
                if cuenta > inventario.cantidad:
                    raise ValueError("No hay suficiente inventario")
                session['carrito'][key_item] = item
        else:
            if cuenta > inventario.cantidad:
                raise ValueError("No hay suficiente inventario")
            session['carrito'] = { key_item: item }
            
        session['total'] = math.ceil(sum(itm['subtotal'] for itm in session['carrito'].values()))
        session['cantidad_total'] = sum(itm['cantidad'] for itm in session['carrito'].values())
        return session['carrito']
    
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
        print("Carrito:", carrito)
        if not carrito:
            return {}, 0
        return carrito, total