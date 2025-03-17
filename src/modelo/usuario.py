from bd import bd
from modelo.rol import Rol

class Usuario(bd.Model):
    __tablename__ = 'usuarios'
    
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(150), nullable=False)
    password = bd.Column(bd.String(50), nullable=False)
    rol_id = bd.Column(bd.Integer, bd.ForeignKey('roles.id'), nullable=False)
    email = bd.Column(bd.String(50), nullable=False)
    
    rol_id = bd.Column(bd.Integer, bd.ForeignKey('roles.id'), nullable=False)
    rol = bd.relationship(Rol, backref='usuarios')