from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('receta', __name__)

trabajador_permission = Permission(RoleNeed('TRABAJADOR'))

@controlador.route('/recetas', methods=['GET', 'POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def recetas():
    return render_template('recetas.html')