from bd import bd

class Proveedor(bd.Model):
    __tablename__ = 'proveedores'
    
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50), nullable=False)
    contacto = bd.Column(bd.String(50), nullable=False)