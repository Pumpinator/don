from bd import bd
from flask_login import UserMixin

class Usuario(UserMixin, bd.Model):
    __tablename__ = 'usuarios'
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50), nullable=False)
    email = bd.Column(bd.String(100), nullable=False, unique=True)
    password = bd.Column(bd.String(512), nullable=False)
    estatus = bd.Column(bd.Boolean, default=True)
    
    rol_id = bd.Column(bd.Integer, bd.ForeignKey('roles.id'), nullable=False)
    rol = bd.relationship('Rol', backref='usuarios')
    
    def is_active(self):
        return self.estatus