from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from bd import bd
from controlador.compra import controlador as controlador_compra
from controlador.galleta import controlador as controlador_galleta
from controlador.insumo import controlador as controlador_insumo
from controlador.merma import controlador as controlador_merma
from controlador.produccion import controlador as controlador_produccion
from controlador.reportes import controlador as controlador_reportes
from controlador.usuario import controlador as controlador_usuario
from controlador.venta import controlador as controlador_venta
from controlador.receta import controlador as controlador_receta
from controlador.proveedor import controlador as controlador_proveedor
from controlador.pedido import controlador as controlador_pedido
from modelo.compra import Compra
from servicio.usuario import UsuarioServicio
from formularios.ingreso import IngresoForm
from formularios.registro import RegistroForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_principal import current_app, identity_loaded, RoleNeed, UserNeed, Permission, identity_changed, Identity, AnonymousIdentity

controlador = Blueprint('principal', __name__)

controlador.register_blueprint(controlador_compra)
controlador.register_blueprint(controlador_proveedor)
controlador.register_blueprint(controlador_receta)
controlador.register_blueprint(controlador_galleta)
controlador.register_blueprint(controlador_insumo)
controlador.register_blueprint(controlador_merma)
controlador.register_blueprint(controlador_produccion)
controlador.register_blueprint(controlador_reportes)
controlador.register_blueprint(controlador_usuario)
controlador.register_blueprint(controlador_venta)
controlador.register_blueprint(controlador_pedido)

login_manager = LoginManager()
login_manager.login_view = 'principal.ingresar'

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))
admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

@controlador.route("/")
def index():
    return render_template('index.html')

@controlador.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    form = IngresoForm()
    if request.method == 'POST':
        form = IngresoForm(request.form)
        if form.validate():
            usuario_servicio = UsuarioServicio(bd)
            try:
                usuario = usuario_servicio.validar_usuario(form.correo.data, form.password.data)
                login_user(usuario, remember=form.recordarme.data)
                identity_changed.send(current_app._get_current_object(), identity=Identity(usuario.id)) 
                flash("Inicio de sesión exitoso.", "success")
                return redirect(url_for('principal.index'))
            except ValueError as e:
                flash(str(e), "danger")
    return render_template('ingresar.html', form=form)
 
@controlador.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistroForm()
    if request.method == 'POST':
        form = RegistroForm(request.form)
        if form.validate():
            usuario_servicio = UsuarioServicio(bd)
            try:
                usuario = usuario_servicio.crear_comprador(form)
                login_user(usuario)
                identity_changed.send(current_app._get_current_object(), identity=Identity(usuario.id))
                flash("Registro exitoso!", "success")
                return redirect(url_for('principal.index'))
            except ValueError as e:
                flash(str(e), "danger")
    return render_template('registrar.html', form=form)

@controlador.route('/salir')
@login_required
def salir():
    logout_user()
    identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())
    return redirect(url_for('principal.index'))

@identity_loaded.connect
def on_identity_loaded(sender, identity):
    identity.user = current_user
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))
    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.upper()))
    elif hasattr(current_user, 'rol') and current_user.rol:
        identity.provides.add(RoleNeed(current_user.rol.nombre.upper()))
        
@login_manager.user_loader
def load_user(user_id):
    try:
        usuario_servicio = UsuarioServicio(bd)
        usuario = usuario_servicio.obtener_usuario(id=user_id)
        if usuario and hasattr(usuario, 'rol'):
            usuario.roles = [usuario.rol.nombre.upper()]
        return usuario
    except Exception as e:
        return None

@controlador.before_request
def log():
    usuario_servicio = UsuarioServicio(bd)
    usuario = usuario_servicio.obtener_usuario(id = current_user.get_id()) if current_user.is_authenticated else None
    current_app.logger.info(
        "Usuario: %s,Rol: %s, Método: %s, Ruta: %s, Args: %s, Form: %s",
        usuario.email if usuario else 'ANÓNIMO',
        usuario.rol.nombre if usuario else 'ANÓNIMO',
        request.method,
        request.path,
        request.args.to_dict(),
        request.form.to_dict()
    )
    
@controlador.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response