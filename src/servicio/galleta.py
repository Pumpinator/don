from modelo.galleta import Galleta
from modelo.medida import Medida
from modelo.galleta_inventario import GalletaInventario
from sqlalchemy import func

class GalletaServicio:
    def __init__ (self, bd):
        self.bd = bd
    
    def obtener_galletas(self):
        return self.bd.session.query(Galleta).all()

    def obtener_inventarios(self):
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