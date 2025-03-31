from bd import bd
from modelo.transaccion import Transaccion
from modelo.proveedor import Proveedor

class Compra(Transaccion, bd.Model):
    __tablename__ = 'compras'
    
    id = bd.Column(bd.Integer, primary_key=True)
    proveedor_id = bd.Column(bd.Integer, bd.ForeignKey('proveedores.id'), nullable=False)
    fecha = bd.Column(bd.Date, nullable=False)  
    
    proveedor = bd.relationship(Proveedor, backref='compras')