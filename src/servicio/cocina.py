from modelo.medida import Medida
from modelo.insumo import Insumo
from modelo.produccion import Produccion
from modelo.galleta import Galleta

class CocinaServicio:
    
    def __init__ (self, bd):
        self.bd=bd
        
    def obtener_insumos(self):
        return self.bd.session.query(Insumo).all()
    
    def obtener_medidas(self):
        return self.bd.session.query(Medida).distinct().all()
    
    def obtener_producciones(self):
        return self.bd.session.query(Produccion).all()
    
    def obtener_galletas(self):
        return self.bd.session.query(Galleta).all()