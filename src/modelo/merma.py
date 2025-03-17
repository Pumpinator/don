from bd import bd
from modelo.medible import Medible
from modelo.produccion import Produccion
from modelo.insumo import Insumo
from modelo.galleta import Galleta

class Merma(Medible, bd.Model):
    __tablename__ = 'mermas'
    
    id = bd.Column(bd.Integer, primary_key=True)
    total = bd.Column(bd.Float, nullable=False)
    
    produccion_id = bd.Column(bd.Integer, bd.ForeignKey('producciones.id'), nullable=True)
    produccion = bd.relationship(Produccion, backref='mermas')
    
    insumo_id = bd.Column(bd.Integer, bd.ForeignKey('insumos.id'), nullable=True)
    insumo = bd.relationship(Insumo, backref='mermas')
    
    galleta_id = bd.Column(bd.Integer, bd.ForeignKey('galletas.id'), nullable=True)
    galleta = bd.relationship(Galleta, backref='mermas')