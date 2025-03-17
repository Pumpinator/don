from modelo.usuario import Usuario

def obtener_usuarios():
    return Usuario.query.all()