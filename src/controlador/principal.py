from flask import Blueprint, render_template, request, flash, redirect, url_for
from bd import bd
from controlador.usuario import controlador as controlador_usuario
from controlador.galleta import controlador as controlador_galleta
from controlador.insumo import controlador as controlador_insumo
from controlador.merma import controlador as controlador_merma
from controlador.venta import controlador as controlador_venta
from controlador.error import controlador as controlador_error
from servicio.usuario import UsuarioServicio
from formularios.ingreso import IngresoForm
from formularios.registro import RegistroForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_principal import current_app, identity_loaded, RoleNeed, UserNeed, Permission, identity_changed, Identity, AnonymousIdentity

controlador = Blueprint('principal', __name__)

controlador.register_blueprint(controlador_usuario)
controlador.register_blueprint(controlador_galleta)
controlador.register_blueprint(controlador_insumo)
controlador.register_blueprint(controlador_merma)
controlador.register_blueprint(controlador_venta)
controlador.register_blueprint(controlador_error)

login_manager = LoginManager()
login_manager.login_view = 'principal.ingresar'

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))

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

@controlador.route('/cuenta')
@login_required
def cuenta():
    return render_template('cuenta.html')

@controlador.route('/salir')
@login_required
def salir():
    logout_user()
    identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())
    return redirect(url_for('principal.index'))

@controlador.route('/compras')
@login_required
@trabajador_permission.require(http_exception=403)
def compras():
    return render_template('compras.html')

@controlador.route('/recetas')
@login_required
@trabajador_permission.require(http_exception=403)
def recetas():
    return render_template('recetas.html')


@controlador.route('/produccion')
@login_required
@trabajador_permission.require(http_exception=403)
def produccion():
	return render_template('produccion.html')

@controlador.route('/reportes')
@login_required
@trabajador_permission.require(http_exception=403)
def reportes():
	return render_template('reportes.html')

@controlador.route('/clientes')
@login_required
@trabajador_permission.require(http_exception=403)
def clientes():
    return render_template('catalogo_cliente.html') 

@controlador.route('/menu')
def menu():
    return render_template('menu.html') 

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
