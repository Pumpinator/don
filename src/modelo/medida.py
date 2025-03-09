from bd import bd

class Medida(bd.Model):
    __tablename__ = 'medidas'
    
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50), nullable=False)