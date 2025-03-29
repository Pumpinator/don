from modelo.produccion import Produccion
from modelo.receta import Receta

class ProduccionServicio:
    
    def __init__ (self, bd):
        self.bd=bd
        
    def obtener_producciones(self):
        return self.bd.session.query(Produccion).all()
    
    def obtener_recetas(self):
        return self.bd.session.query(Receta).all()