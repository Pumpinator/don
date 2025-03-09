from bd import bd

class Receta(bd.Model):
    __tablename__ = 'recetas'
    
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50), nullable=False)
    
    galleta_id = bd.Column(bd.Integer, bd.ForeignKey('galletas.id'), nullable=False)
    galleta = bd.relationship('Galleta', backref='recetas')