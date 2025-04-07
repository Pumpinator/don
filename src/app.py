import logging

from flask import Flask
from flask_principal import Principal
from config import DevelopmentConfig
from controlador.principal import controlador as controlador_principal, login_manager
from bd import bd

app = Flask(__name__, static_folder='vista/static', template_folder='vista/templates')
app.config.from_object(DevelopmentConfig)

handler = logging.FileHandler('app.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

login_manager.init_app(app)
principal = Principal(app)

app.register_blueprint(controlador_principal)

if __name__ == '__main__':
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True, port=3000)