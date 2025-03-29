from modelo.galleta import Galleta
from modelo.galleta_inventario import GalletaInventario
from modelo.medida import Medida
from sqlalchemy import func

class VentaServicio:
    
    def __init__(self, bd):
        self.bd = bd
    
    def obtener_mostrador(self):
        resultados = (
            self.bd.session
            .query(
                Galleta.id,
                Galleta.nombre, 
                func.sum(GalletaInventario.cantidad).label("cantidad_total"),
                func.min(Galleta.precio).label("precio"),
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
                "medida": medida
            }
            for galleta_id, nombre, cantidad_total, precio, medida in resultados
        ]
        return mostrador