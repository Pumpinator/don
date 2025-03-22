from modelo.usuario import Usuario
from modelo.rol import Rol
from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioServicio:
    
    def __init__(self, bd):
        self.bd = bd

    def obtener_usuarios(self):
        return self.bd.session.query(Usuario).all()

    def obtener_usuario(self, id=None, correo=None):
        if id:
            return self.bd.session.query(Usuario).join(Rol).filter(Usuario.id == id).first()
        if correo:
            return self.bd.session.query(Usuario).join(Rol).filter(Usuario.email == correo).first()
        return None

    def crear_comprador(self, form):
        nombre = form.nombre.data
        email = form.email.data
        password = form.password.data
        
        if self.obtener_usuario(correo=email):
            raise ValueError("El correo ya se encuentra registrado.")
        
        rol = self.bd.session.query(Rol).filter(Rol.nombre == "COMPRADOR").first()
            
        hashed = generate_password_hash(password)
        rol = self.bd.session.query(Rol).filter(Rol.nombre == 'COMPRADOR').first()
        usuario = Usuario(nombre=nombre, email=email, password=hashed, rol_id=rol.id)
        
        self.bd.session.add(usuario)
        self.bd.session.commit()
        
        return usuario
    
    def crear_trabajador(self, form):
        nombre = form.nombre.data
        email = form.email.data
        password = form.password.data
        
        if self.obtener_usuario(correo=email):
            raise ValueError("El correo ya se encuentra registrado.")
        
        hash = generate_password_hash(password)
        rol_trabajador = self.bd.session.query(Rol).filter(Rol.nombre == 'TRABAJADOR').first()
        usuario = Usuario(nombre=nombre, email=email, password=hash, rol_id=rol_trabajador.id)
        
        self.bd.session.add(usuario)
        self.bd.session.commit()
        
        return usuario

    def validar_usuario(self, correo, password):
        usuario = self.obtener_usuario(correo=correo)
        if usuario and check_password_hash(usuario.password, password):
            return usuario
        raise ValueError("Credenciales inválidas.")