from bd import bd

class Usuario(bd.Model):
    __tablename__ = 'usuarios'
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50), nullable=False)
    email = bd.Column(bd.String(100), nullable=False, unique=True)
    password = bd.Column(bd.String(100), nullable=False)
    rol_id = bd.Column(bd.Integer, nullable=False)
    estatus = bd.Column(bd.String(20), nullable=False)