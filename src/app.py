from flask import Flask
from config import DevelopmentConfig
from bd import bd
from controlador.usuario import controlador as controlador_usuario
from controlador.galleta import controlador as controlador_galleta
from controlador.insumo import controlador as controlador_insumo
from controlador.principal import controlador as controlador_principal
from controlador.venta import controlador as controlador_venta
from flask_login import LoginManager
from servicio.usuario import UsuarioServicio

app = Flask(__name__, static_folder='vista/static', template_folder='vista/templates')
app.config.from_object(DevelopmentConfig)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'controlador_usuario.ingresar'

@login_manager.user_loader
def load_user(user_id):
    try:
        usuario_servicio = UsuarioServicio(bd)
        usuario = usuario_servicio.obtener_usuario(id=user_id)
        return usuario
    except:
        return None

app.register_blueprint(controlador_principal)
app.register_blueprint(controlador_usuario)
app.register_blueprint(controlador_galleta)
app.register_blueprint(controlador_insumo)
app.register_blueprint(controlador_venta)

if __name__ == '__main__':
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True, port=3000)