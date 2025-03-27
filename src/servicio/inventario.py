from modelo.galleta import Galleta
from modelo.medida import Medida
from modelo.insumo import Insumo
from modelo.insumo_inventario import InsumoInventario
from modelo.galleta_inventario import GalletaInventario
from sqlalchemy import func

class InventarioServicio:
    def __init__ (self, bd):
        self.bd = bd

    def obtener_galletas(self):
        resultados = (
            self.bd.session
            .query(
                Galleta.nombre, 
                func.sum(GalletaInventario.cantidad),
                Medida.nombre
            )
            .join(Galleta, Galleta.id == GalletaInventario.galleta_id)
            .join(Medida, GalletaInventario.medida_id == Medida.id)
            .group_by(Galleta.nombre, Medida.nombre)
            .all()
        )
        inventarios = [
            {"galleta": nombre, "cantidad": int(total), "medida": medida} 
            for nombre, total, medida in resultados
        ]
        return inventarios
    
    def obtener_insumos(self):
        resultados = (
            self.bd.session
            .query(
                Insumo.nombre, 
                func.sum(InsumoInventario.cantidad),
                Medida.nombre
            )
            .join(Insumo, Insumo.id == InsumoInventario.insumo_id)
            .join(Medida, InsumoInventario.medida_id == Medida.id)
            .group_by(Insumo.nombre, Medida.nombre)
            .all()
        )
        inventarios = [
            {"insumo": nombre, "cantidad": int(total), "medida": medida} 
            for nombre, total, medida in resultados
        ]
        return inventarios