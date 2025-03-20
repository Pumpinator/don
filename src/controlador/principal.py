from flask import Blueprint, render_template, request, flash, redirect, url_for
from servicio.usuario import UsuarioServicio
from formularios.ingreso import IngresoForm
from formularios.registro import RegistroForm
from bd import bd
from flask_login import login_user, logout_user

controlador = Blueprint('controlador_principal', __name__)

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
                usuario = usuario_servicio.crear_usuario(form)
                login_user(usuario)
                flash("Registro exitoso!", "success")
                return redirect(url_for('controlador_principal.index'))
            except ValueError as e:
                flash(str(e), "danger")
    return render_template('registrar.html', form=form)

@controlador.route('/cuenta')
def cuenta():
    return render_template('cuenta.html')

@controlador.route('/salir')
def salir():
    logout_user()
    return redirect(url_for('controlador_principal.index'))

@controlador.route('/compras')
def compras():
    return render_template('compras.html')

@controlador.route('/recetas')
def recetas():
    return render_template('recetas.html')

@controlador.route('/mermas')
def mermas():
    return render_template('mermas.html')

@controlador.route('/agregarMerma')
def agregarMerma():
    return render_template('agregarMerma.html')

@controlador.route('/produccion')
def produccion():
	return render_template('produccion.html')

@controlador.route('/reportes')
def reportes():
	return render_template('reportes.html')

@controlador.route('/clientes')
def clientes():
    return render_template('catalogo_cliente.html') 