from flask import Blueprint, render_template

controlador = Blueprint('controlador_principal', __name__)

@controlador.route("/")
def index():
    return render_template('index.html')

@controlador.route('/compras')
def compras():
    return render_template('compras.html')

@controlador.route('/recetas')
def recetas():
    return render_template('recetas.html')

@controlador.route('/mermas')
def mermas():
    return render_template('mermas.html')

@controlador.route('/produccion')
def produccion():
	return render_template('produccion.html')

@controlador.route('/ventas')
def ventas():
    return render_template('ventas.html')

@controlador.route('/reportes')
def reportes():
	return render_template('reportes.html')

@controlador.route('/clientes')
def clientes():
    return render_template('catalogo_cliente.html') 


@controlador.route('/cuenta')
def cuenta():
    return render_template('cuenta.html')