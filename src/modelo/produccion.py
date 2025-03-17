from bd import bd
from modelo.receta import Receta

class Produccion(bd.Model):
    __tablename__ = 'producciones'
    
    id = bd.Column(bd.Integer, primary_key=True)
    fecha = bd.Column(bd.Date, nullable=False)
    costo = bd.Column(bd.Float, nullable=False)
    
    receta_id = bd.Column(bd.Integer, bd.ForeignKey('recetas.id'), nullable=False)
    receta = bd.relationship(Receta, backref='producciones')