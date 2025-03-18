from bd import bd
from modelo.medida import Medida
from sqlalchemy.ext.declarative import declared_attr

class Medible:
    @declared_attr
    def cantidad(cls):
        return bd.Column(bd.Float, nullable=False)

    @declared_attr
    def medida_id(cls):
        return bd.Column(bd.Integer, bd.ForeignKey('medidas.id'), nullable=False)

    @declared_attr
    def medida(cls):
        return bd.relationship(Medida, backref=cls.__name__.lower() + 's')