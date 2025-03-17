from bd import bd
from modelo.medible import Medible
from modelo.receta import Receta
from modelo.insumo import Insumo

class Ingrediente(Medible, bd.Model):
    __tablename__ = 'ingredientes'
    
    receta_id = bd.Column(bd.Integer, bd.ForeignKey('recetas.id'), primary_key=True)
    receta = bd.relationship(Receta, backref='ingredientes')
    
    insumo_id = bd.Column(bd.Integer, bd.ForeignKey('insumos.id'), primary_key=True)
    insumo = bd.relationship(Insumo, backref='ingredientes')