from bd import bd
from modelo.transaccion import Transaccion

class Compra(Transaccion, bd.Model):
    __tablename__ = 'compras'
    
    id = bd.Column(bd.Integer, primary_key=True)
    
    proveedor_id = bd.Column(bd.Integer, bd.ForeignKey('proveedores.id'), nullable=False)
    proveedor = bd.relationship('Proveedor', backref='compras')