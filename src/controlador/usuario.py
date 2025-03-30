from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from servicio.usuario import UsuarioServicio
from formularios.usuario import CrearForm, EditarForm
from bd import bd
from flask_login import login_required, current_user
from flask_principal import Permission, RoleNeed

controlador = Blueprint('usuario', __name__)

admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

@controlador.before_request
def verificar_usuario():
    rol = request.view_args.get('rol')
    print(rol)
    if rol == 'administradores' and current_user.rol.nombre != 'ADMIN':
        abort(403)

@controlador.route('/<rol>/nuevo', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def crear_usuario(rol):
    form = CrearForm()
    if request.method == 'POST' and form.validate():
        form = CrearForm(request.form)
        usuario_servicio = UsuarioServicio(bd)
        try:
            usuario = usuario_servicio.crear_usuario(form)
            flash("Registro exitoso!", "success")
            return redirect(url_for('principal.usuario.listar_usuarios', rol=rol))
        except ValueError as e:
            flash(str(e), "danger")
    return render_template('usuario/crear_usuario.html', form=form, rol=rol)

@controlador.route('/<rol>', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def listar_usuarios(rol):
    usuario_servicio = UsuarioServicio(bd)
    usuarios_list = usuario_servicio.obtener_usuarios(rol=rol)
    return render_template('usuario/usuarios.html', usuarios=usuarios_list, rol=rol)

@controlador.route('/<rol>/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def editar_usuario(rol, id):
    usuario_servicio = UsuarioServicio(bd)
    usuario = usuario_servicio.obtener_usuario(id=id)
    
    form = EditarForm(obj=usuario)
    form.rol.choices.insert(0, [None, "Selecciona un rol..."])
    form.rol.data = usuario.rol.nombre
    
    if request.method == 'POST' and form.validate():
        form = EditarForm(request.form)
        form.rol.choices.insert(0, [None, "Selecciona un rol..."])
        try:
            usuario = usuario_servicio.editar_usuario(form)
            flash("Usuario actualizado exitosamente", "success")
            return redirect(url_for('principal.usuario.listar_usuarios', rol=rol))
        except ValueError as e:
            flash(str(e), "danger")
    return render_template('usuario/editar_usuario.html', form=form, usuario=usuario, rol=rol)

@controlador.route('/<rol>/desactivar/<int:id>', methods=['POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def desactivar_usuario(rol, id):
    usuario_servicio = UsuarioServicio(bd)
    try:
        usuario_servicio.desactivar_usuario(id)
        flash("Usuario desactivado exitosamente", "info")
        return redirect(url_for('usuario.listar_usuarios', rol=rol))
    except ValueError as e:
        flash(str(e), "danger")
    return redirect(url_for('usuario.listar_usuarios', rol=rol))

@controlador.route('/<rol>/activar/<int:id>', methods=['POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def activar_usuario(rol, id):
    usuario_servicio = UsuarioServicio(bd)
    try:
        usuario_servicio.activar_usuario(id)
        flash("Usuario activado exitosamente", "success")
        return redirect(url_for('usuario.listar_usuarios', rol=rol))
    except ValueError as e:
        flash(str(e), "danger")
    return redirect(url_for('usuario.listar_usuarios', rol=rol))
