from bd import bd
from modelo.medida import Medida

class Galleta(bd.Model):
    __tablename__ = 'galletas'
    
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50), nullable=False)
    precio = bd.Column(bd.Float, nullable=False)
    imagen = bd.Column(bd.String(100), nullable=True)
    
    medida_id = bd.Column(bd.Integer, bd.ForeignKey('medidas.id'), nullable=False)
    medida = bd.relationship(Medida, backref='galletas')