from flask import Blueprint, render_template, request, flash, redirect, url_for
from servicio.usuario import UsuarioServicio
from formularios.ingreso import IngresoForm
from formularios.registro import RegistroForm
from bd import bd
from flask_login import login_user, logout_user, login_required
from flask_principal import Permission, RoleNeed, Identity, identity_changed, current_app, AnonymousIdentity

controlador = Blueprint('controlador_principal', __name__)

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
                return redirect(url_for('controlador_principal.index'))
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
                return redirect(url_for('controlador_principal.index'))
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
    return redirect(url_for('controlador_principal.index'))

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

@controlador.route('/mermas')
@login_required
@trabajador_permission.require(http_exception=403)
def mermas():
    return render_template('mermas.html')

@controlador.route('/agregar_merma')
@login_required
@trabajador_permission.require(http_exception=403)
def agregarMerma():
    return render_template('agregar_merma.html')

@controlador.route('/produccion')
@login_required
@admin_permission.require(http_exception=403)
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