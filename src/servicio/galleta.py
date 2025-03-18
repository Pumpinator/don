from modelo.galleta import Galleta
from modelo.galleta_inventario import GalletaInventario

def obtener_galletas():
    return Galleta.query.all()

def obtener_inventarios():
    return GalletaInventario.query.all()