from bd import bd
from modelo.insumo import Insumo
from modelo.medida import Medida

class Ingrediente(bd.Model):
    receta_id = bd.Column(bd.Integer, bd.ForeignKey('recetas.id'), primary_key=True)
    insumo_id = bd.Column(bd.Integer, bd.ForeignKey('insumos.id'), primary_key=True)
    medida_id = bd.Column(bd.Integer, bd.ForeignKey('medidas.id'))
    cantidad = bd.Column(bd.Float)

    # Relación con Insumo
    insumo = bd.relationship('Insumo', backref='ingredientes')
    medida = bd.relationship('Medida', backref='ingredientes')