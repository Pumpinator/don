from collections import defaultdict
from sqlalchemy import func
from modelo.compra_detalle import CompraDetalle
from modelo.galleta_inventario import GalletaInventario
from modelo.produccion import Produccion
from modelo.receta import Receta
from sqlalchemy.orm import joinedload
from datetime import timedelta

class ProduccionServicio:
    
    def __init__(self, bd):
        self.bd = bd
        
    def obtener_producciones(self):
        return self.bd.session.query(Produccion).options(joinedload(Produccion.receta)).all()
    
    def crear_produccion(self, receta_id, fecha, kilos):
        try:
            receta = (
                self.bd.session.query(Receta)
                .options(joinedload(Receta.ingredientes))
                .get(receta_id)
            )
            
            costo_total = 0
            for ingrediente in receta.ingredientes:
                ultima_compra = (
                    self.bd.session.query(CompraDetalle)
                    .filter_by(insumo_id=ingrediente.insumo_id)
                    .order_by(CompraDetalle.compra_id.desc())
                    .first()
                )
                
                if not ultima_compra:
                    raise ValueError(f"Sin compras registradas para {ingrediente.insumo.nombre}")
                
                costo_unitario = ultima_compra.precio_unitario / ultima_compra.cantidad
                costo_total += costo_unitario * ingrediente.cantidad * kilos
            
            nueva_produccion = Produccion(
                fecha=fecha,
                costo=round(costo_total, 2),
                estatus=1,
                receta_id=receta_id
            )
            
            self.bd.session.add(nueva_produccion)
            self.bd.session.commit()
            return nueva_produccion
        except Exception as e:
            self.bd.session.rollback()
            raise e

    def avanzar_estatus(self, produccion_id):
        produccion = self.bd.session.query(Produccion).get(produccion_id)
        if produccion and produccion.estatus < 4:
            produccion.estatus += 1
            
            if produccion.estatus == 4:
                # Recalcular costo base para obtener los kilos
                costo_base = self._calcular_costo_base(produccion.receta)
                kilos = produccion.costo / costo_base if costo_base > 0 else 0
                cantidad_galletas = round(kilos / 0.05)
                
                nuevo_inventario = GalletaInventario(
                    fecha_expiracion=produccion.fecha + timedelta(days=7),
                    costo=produccion.costo,
                    cantidad=cantidad_galletas,
                    medida_id=1,
                    produccion_id=produccion.id,
                    galleta_id=produccion.receta.galleta_id
                )
                self.bd.session.add(nuevo_inventario)
            
            self.bd.session.commit()

    def _calcular_costo_base(self, receta):
        costo_base = 0
        for ingrediente in receta.ingredientes:
            ultima_compra = (
                self.bd.session.query(CompraDetalle)
                .filter_by(insumo_id=ingrediente.insumo_id)
                .order_by(CompraDetalle.compra_id.desc())
                .first()
            )
            
            if ultima_compra:
                costo_unitario = ultima_compra.precio_unitario / ultima_compra.cantidad
                costo_base += costo_unitario * ingrediente.cantidad
        
        return costo_base