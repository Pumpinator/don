from bd import bd
from sqlalchemy.ext.declarative import declared_attr
from modelo.medible import Medible

class TransaccionDetalle(Medible):
    
    @declared_attr
    def precio_unitario(cls):
        return bd.Column(bd.Float, nullable=False)
    
    @declared_attr
    def precio_total(cls):
        return bd.Column(bd.Float, nullable=False)