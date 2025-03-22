from flask import Flask, render_template
from config import DevelopmentConfig
from bd import bd
from controlador.usuario import controlador as controlador_usuario
from controlador.galleta import controlador as controlador_galleta
from controlador.insumo import controlador as controlador_insumo
from controlador.principal import controlador as controlador_principal
from controlador.venta import controlador as controlador_venta
from flask_login import LoginManager, current_user
from flask_principal import Principal, identity_loaded, RoleNeed, UserNeed, Permission
from servicio.usuario import UsuarioServicio

app = Flask(__name__, static_folder='vista/static', template_folder='vista/templates')
app.config.from_object(DevelopmentConfig)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'controlador_usuario.ingresar'

principals = Principal(app)

admin_permission = Permission(RoleNeed('ADMIN'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))
vendedor_permission = Permission(RoleNeed('VENDEDOR'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user

    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role))
    elif hasattr(current_user, 'rol') and current_user.rol:
        identity.provides.add(RoleNeed(current_user.rol.nombre))

@login_manager.user_loader
def load_user(user_id):
    try:
        usuario_servicio = UsuarioServicio(bd)
        usuario = usuario_servicio.obtener_usuario(id=user_id)
        if usuario and hasattr(usuario, 'rol'):
            usuario.roles = [usuario.rol.nombre]
        return usuario
    except Exception as e:
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