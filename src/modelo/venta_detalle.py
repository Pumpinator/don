from bd import bd
from modelo.transaccion_detalle import TransaccionDetalle

class VentaDetalle(TransaccionDetalle, bd.Model):
    __tablename__ = 'ventas_detalles'
    
    venta_id = bd.Column(bd.Integer, bd.ForeignKey('ventas.id'), primary_key=True)
    venta = bd.relationship('Venta', backref='detalles')
    
    galleta_id = bd.Column(bd.Integer, bd.ForeignKey('galletas.id'), primary_key=True)
    galleta = bd.relationship('Galleta', backref='detalles')