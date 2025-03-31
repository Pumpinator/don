from bd import bd
from modelo.transaccion import Transaccion
from modelo.usuario import Usuario

class Venta(Transaccion, bd.Model):
    __tablename__ = 'ventas'
    
    id = bd.Column(bd.Integer, primary_key=True)
    pagado = bd.Column(bd.Boolean, default=False, nullable=False)
    fecha_entrega = bd.Column(bd.Date, nullable=False)
    
    comprador_id = bd.Column(bd.Integer, bd.ForeignKey('usuarios.id'), nullable=True)
    comprador = bd.relationship(Usuario, foreign_keys=[comprador_id], backref='compras_realizadas')
    
    vendedor_id = bd.Column(bd.Integer, bd.ForeignKey('usuarios.id'), nullable=False)
    vendedor = bd.relationship(Usuario, foreign_keys=[vendedor_id], backref='ventas_realizadas')