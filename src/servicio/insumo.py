from modelo.insumo_inventario import InsumoInventario
from modelo.insumo import Insumo


class InsumoServicio:
    def __init__(self, bd):
        self.bd = bd
     
    def obtener_insumos(self):
        return self.bd.session.query(Insumo).all()
    
    def obtener_inventario(self):
        return self.bd.session.query(InsumoInventario).all()
