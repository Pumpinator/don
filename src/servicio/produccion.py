from collections import defaultdict
from sqlalchemy import func
from modelo.compra_detalle import CompraDetalle
from modelo.produccion import Produccion
from modelo.receta import Receta
from modelo.ingrediente import Ingrediente
from modelo.insumo import Insumo
from modelo.galleta import Galleta
from modelo.medida import Medida
from sqlalchemy.orm import joinedload

class ProduccionServicio:
    
    def __init__(self, bd):
        self.bd = bd
        
    def obtener_producciones(self):
        return self.bd.session.query(Produccion).options(joinedload(Produccion.receta)).all()
    
    def avanzar_estatus(self, produccion_id):
        produccion = self.bd.session.query(Produccion).filter_by(id=produccion_id).first()
        if produccion and produccion.estatus < 4:
            produccion.estatus += 1 
            self.bd.session.commit()

    def crear_produccion(self, receta_id, fecha):
        try:
            # Obtener receta con ingredientes
            receta = (
                self.bd.session.query(Receta)
                .options(joinedload(Receta.ingredientes))
                .get(receta_id)
            )
            
            # Calcular costo
            costo_total = 0
            for ingrediente in receta.ingredientes:
                # Obtener último precio del insumo
                ultima_compra = (
                    self.bd.session.query(CompraDetalle)
                    .filter_by(insumo_id=ingrediente.insumo_id)
                    .order_by(CompraDetalle.compra_id.desc())
                    .first()
                )
                
                if not ultima_compra:
                    raise ValueError(f"Sin compras registradas para {ingrediente.insumo.nombre}")
                
                # Calcular costo unitario
                costo_unitario = ultima_compra.precio_unitario / ultima_compra.cantidad
                costo_total += costo_unitario * ingrediente.cantidad
            
            # Crear producción
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