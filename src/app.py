from flask import Flask, render_template, request, redirect, url_for
from config import DevelopmentConfig
from bd import bd
from repositorio import *
import forms
from modelo.usuario import Usuario

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/compras')
def compras():
    return render_template('compras.html')

@app.route('/insumos')
def insumos():
    insumos=[
        "harina",
        "azucar",
        "huevo",
        "leche",
        "mantequilla",
        "chocolate",
        "canela",
        "vainilla",
        "sal",
        "royal",
        "coco",
        "almendra",
        "nuez",
        "cacahuate",
        "fresa",
        "pasas",
        "avellana",
        "chispas",
        "avena",
        "colorante",]
    return render_template('insumos.html', insumos=insumos)

@app.route('/recetas')
def recetas():
    return render_template('recetas.html')

@app.route('/galletas')
def galletas():
    galletas = [
        "chispas",
        "avellana",
        "almendra",
        "avena",
        "coco",
        "cacahuate",
        "nuez",
        "pasas",
        "mantequilla",
        "fresa",
    ]
    return render_template('galletas.html', galletas=galletas )

@app.route('/mermas')
def mermas():
    return render_template('mermas.html')

@app.route('/produccion')
def produccion():
	return render_template('produccion.html')

@app.route('/ventas')
def ventas():
    return render_template('ventas.html')

@app.route('/reportes')
def reportes():
	return render_template('reportes.html')

@app.route('/clientes')
def clientes():
    return render_template('catalogo_cliente.html') 

@app.route('/usuarios')
def usuarios():
	return render_template('usuarios.html')

@app.route('/cuenta')
def cuenta():
    return render_template('cuenta.html')

@app.route('/crear_cuenta', methods=['GET', 'POST'])
def crear_cuenta():
    form=forms.UseForm(request.form)
    if request.method == 'POST':
        usuario = Usuario(nombre=form.nombre.data + " " + form.apellido.data
                          , email=form.email.data
                          , password=form.contrasenia.data
                          , rol_id='3'
                          ,estatus = '1')
        bd.session.add(usuario)
        bd.session.commit()
        return redirect(url_for("index"))
    return render_template('crear_cuenta.html', form=form)

if __name__ == '__main__':
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True, port=3000)