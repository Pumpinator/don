from modelo.insumo_inventario import InsumoInventario
from modelo.insumo import Insumo

class InsumoServicio:
    
    def __init__ (self, bd):
        self.bd=bd
    
    def obtener_insumos():
        return Insumo.query.all()