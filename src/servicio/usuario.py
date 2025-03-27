from modelo.usuario import Usuario
from modelo.rol import Rol
from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioServicio:
    
    def __init__(self, bd):
        self.bd = bd

    def obtener_usuarios(self, rol=None):
        if rol:
            rol_obj = self.bd.session.query(Rol).filter(Rol.nombre == cast_role(rol)).first()
            if rol_obj:
                return self.bd.session.query(Usuario).filter(Usuario.rol_id == rol_obj.id).all()
            else:
                return []
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
    
    def crear_usuario(self, form):
        nombre = form.nombre.data
        email = form.email.data
        password = form.password.data
        print(form.rol.data)
        
        if self.obtener_usuario(correo=email):
            raise ValueError("El correo ya se encuentra registrado.")
        
        hash = generate_password_hash(password)
        rol = self.bd.session.query(Rol).filter(Rol.nombre == cast_role(form.rol.data)).first()
        usuario = Usuario(nombre=nombre, email=email, password=hash, rol_id=rol.id)
        
        self.bd.session.add(usuario)
        self.bd.session.commit()
        
        return usuario

    def validar_usuario(self, correo, password):
        usuario = self.obtener_usuario(correo=correo)
        if not usuario:
            raise ValueError("Usuario no encontrado.")
        if not check_password_hash(usuario.password, password):
            raise ValueError("Credenciales inválidas.")
        if not usuario.estatus:
            raise ValueError("Usuario desactivado.")
        return usuario
    
    def editar_usuario(self, form):
        id= form.id.data
        nombre = form.nombre.data
        email = form.email.data
        password = form.password.data
        rol = form.rol.data
        print(rol)
        
        usuario = self.obtener_usuario(id=id)
        
        if not usuario:
            raise ValueError("Usuario no encontrado.")
        
        if email != usuario.email and self.obtener_usuario(correo=email):
            raise ValueError("El correo ya se encuentra registrado.")
        
        if password:
            usuario.password = generate_password_hash(password)
        
        usuario.nombre = nombre
        usuario.email = email
        usuario.rol_id = self.bd.session.query(Rol).filter(Rol.nombre == rol).first().id
        
        self.bd.session.commit()
        return usuario
    
    def desactivar_usuario(self, id):
        usuario = self.obtener_usuario(id=id)
        if not usuario:
            raise ValueError("Usuario no encontrado.")
        usuario.estatus = False
        self.bd.session.commit()
        return usuario.estatus
    
    def activar_usuario(self, id):
        usuario = self.obtener_usuario(id=id)
        if not usuario:
            raise ValueError("Usuario no encontrado.")
        usuario.estatus = True
        self.bd.session.commit()
        return usuario.estatus

def cast_role(role):
    mapping = {
        'administradores': 'ADMIN',
        'trabajadores': 'TRABAJADOR',
        'compradores': 'COMPRADOR'
    }
    return mapping.get(role.lower())