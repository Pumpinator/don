from flask import Flask, render_template
from config import DevelopmentConfig
from bd import bd
from controlador.usuario import controlador as controlador_usuario
from controlador.galletas import controlador as controlador_galleta
from controlador.insumo import controlador as controlador_insumo
from controlador.principal import controlador as controlador_principal

app = Flask(__name__, static_folder='vista/static', template_folder='vista/templates')
app.config.from_object(DevelopmentConfig)

app.register_blueprint(controlador_principal)
app.register_blueprint(controlador_usuario)
app.register_blueprint(controlador_galleta)
app.register_blueprint(controlador_insumo)

if __name__ == '__main__':
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True, port=3000)