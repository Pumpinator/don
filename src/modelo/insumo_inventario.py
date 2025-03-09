from bd import bd
from modelo.inventario import Inventario

class InsumoInventario(Inventario, bd.Model):
    __tablename__ = 'insumos_inventarios'
    
    compra_id = bd.Column(bd.Integer, bd.ForeignKey('compras.id'), primary_key=True)
    compra = bd.relationship('Compra', backref='insumos_inventario')
    
    insumo_id = bd.Column(bd.Integer, bd.ForeignKey('insumos.id'), primary_key=True)
    insumo = bd.relationship('Insumo', backref='inventarios')