from bd import bd
from sqlalchemy.ext.declarative import declared_attr
from modelo.medible import Medible

class Inventario(Medible):
    @declared_attr
    def fecha_expiracion(cls):
        return bd.Column(bd.Date, nullable=False)
    
    @declared_attr
    def costo(cls):
        return bd.Column(bd.Float, nullable=False)