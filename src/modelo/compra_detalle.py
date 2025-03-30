from bd import bd
from modelo.transaccion_detalle import TransaccionDetalle
from modelo.insumo import Insumo
from modelo.compra import Compra

class CompraDetalle(TransaccionDetalle, bd.Model):
    __tablename__ = 'compras_detalles'
    
    compra_id = bd.Column(bd.Integer, bd.ForeignKey('compras.id'), primary_key=True)
    compra = bd.relationship(Compra, backref='detalles')
    
    insumo_id = bd.Column(bd.Integer, bd.ForeignKey('insumos.id'), primary_key=True)
    insumo = bd.relationship(Insumo, backref='detalles')

    cantidad = bd.Column(bd.Float, nullable=False) 
    precio_unitario = bd.Column(bd.Float, nullable=False)  
    precio_total = bd.Column(bd.Float, nullable=False) 
    medida_id = bd.Column(bd.Integer, bd.ForeignKey('medidas.id'), nullable=False)  
    medida = bd.relationship('Medida', backref='detalles')  

    def __init__(self, compra_id, insumo_id, cantidad, precio_unitario, medida_id):
        self.compra_id = compra_id
        self.insumo_id = insumo_id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.precio_total = float(cantidad) * float(precio_unitario),
        self.medida_id = medida_id