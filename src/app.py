from flask import Flask
from config import DevelopmentConfig
from bd import bd
from repositorio import *
from modelo.usuario import Usuario
from controlador.usuario import controlador as controlador_usuario
from controlador.galleta import controlador as controlador_galleta
from controlador.insumo import controlador as controlador_insumo
from controlador.principal import controlador as controlador_principal
from controlador.venta import controlador as controlador_venta
from repositorio import *
import pymysql

app = Flask(__name__, static_folder='vista/static', template_folder='vista/templates')
app.config.from_object(DevelopmentConfig)

connection = pymysql.connect(host='localhost', user='root', password='password')
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS dongalleto")
cursor.close()
connection.close()


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