from collections import defaultdict
from sqlalchemy import func
from modelo.compra_detalle import CompraDetalle
from modelo.galleta_inventario import GalletaInventario
from modelo.insumo_inventario import InsumoInventario
from modelo.produccion import Produccion
from modelo.receta import Receta
from sqlalchemy.orm import joinedload
from datetime import datetime, timedelta

class ProduccionServicio:
    
    def __init__(self, bd):
        self.bd = bd
        
    def obtener_producciones(self):
        return self.bd.session.query(Produccion).options(joinedload(Produccion.receta).joinedload(Receta.galleta)).all()
    
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
            
            if produccion.estatus == 3:
                try:
                    costo_base = self._calcular_costo_base(produccion.receta)
                    kilos = float(produccion.costo) / costo_base if costo_base > 0 else 0
                    
                    for ingrediente in produccion.receta.ingredientes:
                        insumo_id = ingrediente.insumo_id
                        cantidad_necesaria = ingrediente.cantidad * kilos
                        
                        lotes = (
                            self.bd.session.query(InsumoInventario)
                            .filter(
                                InsumoInventario.insumo_id == insumo_id,
                                InsumoInventario.fecha_expiracion >= datetime.today().date(),
                                InsumoInventario.cantidad > 0
                            )
                            .order_by(InsumoInventario.fecha_expiracion.asc())
                            .all()
                        )
                        
                        total_disponible = sum(lote.cantidad for lote in lotes)
                        if total_disponible < cantidad_necesaria:
                            raise ValueError(f"Insumo {ingrediente.insumo.nombre} insuficiente: Requerido {round(cantidad_necesaria, 2)}, Disponible {round(total_disponible, 2)}")
                        
                        restante = cantidad_necesaria
                        for lote in lotes:
                            if restante <= 0:
                                break
                            a_restar = min(lote.cantidad, restante)
                            lote.cantidad -= a_restar
                            restante -= a_restar
                            if lote.cantidad == 0:
                                self.bd.session.delete(lote)
                    
                    cantidad_galletas = round(kilos / 0.05)
                    nuevo_inventario = GalletaInventario(
                        fecha_expiracion=produccion.fecha + timedelta(days=7),
                        costo=produccion.costo,
                        cantidad=cantidad_galletas,
                        medida_id=3,
                        produccion_id=produccion.id,
                        galleta_id=produccion.receta.galleta_id
                    )
                    self.bd.session.add(nuevo_inventario)
                    self.bd.session.commit()
                
                except Exception as e:
                    self.bd.session.rollback()
                    raise e
            else:
                self.bd.session.commit()
        else:
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