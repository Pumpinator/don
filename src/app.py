from flask import Flask
from config import DevelopmentConfig
from bd import bd
from controlador.principal import controlador as controlador_principal, login_manager
from flask_principal import Principal

app = Flask(__name__, static_folder='vista/static', template_folder='vista/templates')
app.config.from_object(DevelopmentConfig)

login_manager.init_app(app)
principal = Principal(app)

app.register_blueprint(controlador_principal)

if __name__ == '__main__':
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True, port=3000)