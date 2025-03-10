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