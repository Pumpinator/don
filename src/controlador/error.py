from flask import Blueprint, render_template

controlador = Blueprint('error', __name__)

@controlador.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@controlador.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403