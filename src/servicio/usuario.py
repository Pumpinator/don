from modelo.usuario import Usuario

def obtener_usuarios():
    return Usuario.query.all()

def crear_usuario(nombre, correo, contrasena):
    usuario = Usuario(nombre=nombre, correo=correo, contrasena=contrasena)
    usuario.save()
    return usuario