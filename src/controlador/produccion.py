from flask import Blueprint, render_template
from sqlalchemy import text
from servicio.produccion import ProduccionServicio
from bd import bd
from flask_login import login_required
from flask_principal import Permission, RoleNeed
from flask import Blueprint, render_template, request, redirect, url_for
from modelo.galleta import Galleta
from modelo.insumo import Insumo
from modelo.medida import Medida
from modelo.receta import Receta
from modelo.ingrediente import Ingrediente
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('produccion', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))
admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))

@controlador.route('/produccion')
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def produccion():
    produccion_servicio = ProduccionServicio(bd)
    producciones = produccion_servicio.obtener_producciones()
    return render_template('produccion/produccion.html', produccion=producciones)

@controlador.route('/produccion/avanzar/<int:produccion_id>', methods=['POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def avanzar_produccion(produccion_id):
    produccion_servicio = ProduccionServicio(bd)
    produccion_servicio.avanzar_estatus(produccion_id)
    return redirect(url_for('principal.produccion.produccion'))

