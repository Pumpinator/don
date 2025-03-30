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
        
        galleta = self.obtener_galleta(galleta_id)
        if not galleta:
            raise ValueError("Galleta no encontrada")
        
        presentaciones = {
            "1 pz": 0.05,
            "2 pz": 0.1,
            "5 pz": 0.25,
            "100 g": 0.1,
            "250 g": 0.25,
            "500 g": 0.5,
            "1 kg": 1
        }
        
        peso = presentaciones.get(presentacion)
        unidad = re.sub(r'^[0-9\s]+', '', presentacion).strip()
        key_item = f"{galleta.nombre} {presentacion}"
        item = {
            'galleta_id': galleta_id,
            'nombre': galleta.nombre,
            'presentacion': presentacion,
            'unidad': unidad,
            'peso': peso,
            'precio': galleta.precio,
            'medida_id': medida_id,
            'cantidad': 1,
            'subtotal': (peso / 0.05) * galleta.precio,
            'imagen': galleta.imagen,
        }
        
        session.modified = True
        if 'carrito' in session:
            if key_item in session['carrito']:
                # Actualizar datos generales del producto en el carrito
                old_qty = session['carrito'][key_item]['peso']
                new_qty = old_qty + peso
                session['carrito'][key_item]['peso'] = new_qty
                session['carrito'][key_item]['subtotal'] = (new_qty / 0.05) * galleta.precio
                session['carrito'][key_item]['cantidad'] += 1
            else:
                session['carrito'][key_item] = item
                # Agregar nuevo producto al carrito
                session['carrito'][key_item]['subtotal'] = (peso / 0.05) * galleta.precio
                session['carrito'][key_item]['cantidad'] = 1
                session['carrito'][key_item]['peso'] = peso
                session['carrito'][key_item]['medida_id'] = medida_id
                session['carrito'][key_item]['galleta_id'] = galleta_id
                session['carrito'][key_item]['nombre'] = galleta.nombre
                session['carrito'][key_item]['presentacion'] = presentacion
                session['carrito'][key_item]['precio'] = galleta.precio
                session['carrito'][key_item]['imagen'] = galleta.imagen
        # Si no existe el carrito, crear uno nuevo
        else:
            session['carrito'] = { key_item: item }
        
        # Actualizar totales del carrito, redondeando el total hacia arriba
        session['total'] = math.ceil(sum(itm['subtotal'] for itm in session['carrito'].values()))
        session['cantidad_total'] = sum(itm['cantidad'] for itm in session['carrito'].values())
        
        return session['carrito']
    
    def obtener_carrito(self, session):
        carrito = session.get('carrito', {})
        total = math.ceil(session.get('total', 0))
        if not carrito:
            return {}, 0
        return carrito, total