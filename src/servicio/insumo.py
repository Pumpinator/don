from modelo.insumo import Insumo

def obtener_insumos():
    return Insumo.query.all()