from flask import Flask, render_template
from config import DevelopmentConfig
from modelos import bd

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/compras')
def compras():
    return render_template('compras.html')

@app.route('/insumos')
def insumos():
    return render_template('insumos.html')

@app.route('/recetas')
def recetas():
    return render_template('recetas.html')

@app.route('/galletas')
def galletas():
    return render_template('galletas.html')

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

if __name__ == '__main__':
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True, port=3000)