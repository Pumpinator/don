from bd import bd
from sqlalchemy.ext.declarative import declared_attr

class Transaccion:
    @declared_attr
    def fecha(cls):
        return bd.Column(bd.Date, nullable=False)