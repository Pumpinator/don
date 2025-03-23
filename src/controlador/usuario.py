from flask import Blueprint, render_template, request, flash, redirect, url_for
from servicio.usuario import UsuarioServicio
from formularios.usuario import UsuarioForm
from bd import bd
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('controlador_usuario', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))

@controlador.route('/<rol>/nuevo', methods=['GET', 'POST'])
@login_required
@admin_permission.require(http_exception=403)
def nuevo(rol):
    form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.form)
        if form.validate():
            usuario_servicio = UsuarioServicio(bd)
            try:
                usuario = usuario_servicio.crear_usuario(form)
                flash("Registro exitoso!", "success")
                return redirect(url_for('controlador_usuario.usuarios', rol=rol))
            except ValueError as e:
                flash(str(e), "danger")
    return render_template('crear_usuario.html', form=form, rol=rol)

@controlador.route('/<rol>')
@login_required
@admin_permission.require(http_exception=403)
def usuarios(rol):
    usuario_servicio = UsuarioServicio(bd)
    usuarios_list = usuario_servicio.obtener_usuarios(rol=rol)
    return render_template('usuarios.html', usuarios=usuarios_list, rol=rol)

@controlador.route('/<rol>/<int:id>')
@login_required
@admin_permission.require(http_exception=403)
def usuario(rol, id):
    usuario_servicio = UsuarioServicio(bd)
    usuario = usuario_servicio.obtener_usuario(id=id)
    return render_template('usuario.html', usuario=usuario)