from bd import bd
from modelo.inventario import Inventario

class GalletaInventario(Inventario, bd.Model):
    __tablename__ = 'galletas_inventarios'
    
    produccion_id = bd.Column(bd.Integer, bd.ForeignKey('producciones.id'), primary_key=True)
    produccion = bd.relationship('Produccion', backref='galletas_inventario')
    
    galleta_id = bd.Column(bd.Integer, bd.ForeignKey('galletas.id'), primary_key=True)
    galleta = bd.relationship('Galleta', backref='inventarios')