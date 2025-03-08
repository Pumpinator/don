from flask_sqlalchemy import SQLAlchemy

bd = SQLAlchemy()

class Insumo(bd.Model):
    __tablename__ = 'insumos'
    
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50), nullable=False)
    
class Receta(bd.Model):
    __tablename__ = 'recetas'
    
    id = bd.Column(bd.Integer, primary_key=True)
    insumos = bd.relationship('Insumo', secondary='insumos_recetas')
    
class InsumoReceta(bd.Model):
    __tablename__ = 'insumos_recetas'
    
    insumo_id = bd.Column(bd.Integer, bd.ForeignKey('insumos.id'), primary_key=True)
    receta_id = bd.Column(bd.Integer, bd.ForeignKey('recetas.id'), primary_key=True)