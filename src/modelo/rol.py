from bd import bd

class Rol(bd.Model):
    __tablename__ = 'roles'
    
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50), nullable=False)