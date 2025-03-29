from modelo.medida import Medida
from modelo.insumo import Insumo
from modelo.insumo_inventario import InsumoInventario
from modelo.galleta import Galleta
from modelo.produccion import Produccion
from sqlalchemy import func

class CocinaServicio:
    
    def __init__ (self, bd):
        self.bd=bd
        
    def obtener_insumos(self):
        resultados = (
            self.bd.session.query(
                Insumo.nombre,
                func.sum(InsumoInventario.cantidad).label("cantidad_total"),
                InsumoInventario.medida
            )
            .join(Insumo, Insumo.id == InsumoInventario.insumo_id)
            .join(Medida, InsumoInventario.medida_id == Medida.id)
            .group_by(Insumo.nombre, InsumoInventario.medida)
            .all()
        )
        inventarios = [
            {"insumo": nombre, "cantidad": int(cantidad_total), "medida": medida} 
            for nombre, cantidad_total, medida in resultados
        ]
        return inventarios
    
    def obtener_medidas(self):
        return self.bd.session.query(Medida).distinct().all()
    
    def obtener_producciones(self):
        return self.bd.session.query(Produccion).all()
    
    def obtener_galletas(self):
        return self.bd.session.query(Galleta).all()

    def agregar_insumo(self, form):
        nombre = form.get('nombre')
        insumo = Insumo(nombre = nombre)
        self.bd.session.add(insumo)  
        self.bd.session.commit()