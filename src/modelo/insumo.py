from bd import bd

class Insumo(bd.Model):
    __tablename__ = 'insumos'
    
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50), nullable=False)