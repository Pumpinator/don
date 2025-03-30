from bd import bd
from modelo.galleta import Galleta
from modelo.ingrediente import Ingrediente

class Receta(bd.Model):
    __tablename__ = 'recetas'
    
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50), nullable=False)
    procedimiento = bd.Column(bd.Text, nullable=False)
    galleta_id = bd.Column(bd.Integer, bd.ForeignKey('galletas.id'), nullable=False)
    galleta = bd.relationship(Galleta, backref='recetas')

    ingredientes = bd.relationship('Ingrediente', backref='receta', lazy=True)
