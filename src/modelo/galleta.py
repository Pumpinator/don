from bd import bd

class Galleta(bd.Model):
    __tablename__ = 'galletas'
    
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50), nullable=False)
    precio = bd.Column(bd.Float, nullable=False)