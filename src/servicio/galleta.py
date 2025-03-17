from modelo.galleta import Galleta

def obtener_galletas():
    return Galleta.query.all()