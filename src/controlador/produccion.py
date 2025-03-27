<<<<<<< HEAD
from flask import Blueprint, render_template
from servicio.produccion import ProduccionServicio
from bd import bd
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('controlador_produccion', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))
admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))


@controlador.route('/produccion')
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def recetas():
    servicio_produccion = ProduccionServicio(bd)  # Crear una instancia del servicio
    recetas = servicio_produccion.obtener_recetas()  # Llamar al método de instancia correctamente
    return render_template('produccion.html', recetas=recetas)
=======
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('produccion', __name__)

trabajador_permission = Permission(RoleNeed('TRABAJADOR'))

@controlador.route('/produccion', methods=['GET', 'POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def produccion():
    return render_template('produccion.html')
>>>>>>> 915c88a72e47495dea5d9593218cecb790f53421
