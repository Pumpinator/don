from fileinput import filename
import logging
import os
from flask import Flask, render_template
from flask_principal import Principal
from config import DevelopmentConfig
from controlador.principal import controlador as controlador_principal, login_manager
from bd import bd

app = Flask(__name__, static_folder='vista/static', template_folder='vista/templates')
app.config.from_object(DevelopmentConfig)
app.config['UPLOAD_FOLDER'] = os.path.join('src','vista', 'static', 'img')

filename = "example.txt"  # Define un nombre de archivo válido
filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

handler = logging.FileHandler('app.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

login_manager.init_app(app)
principal = Principal(app)

app.register_blueprint(controlador_principal)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403


if __name__ == '__main__':
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True, port=3000)