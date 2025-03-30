from collections import defaultdict
from sqlalchemy import func
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
