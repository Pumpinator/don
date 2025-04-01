from flask import Blueprint, render_template, request, redirect, url_for, flash
from bd import bd
from servicio.merma import MermaServicio
from servicio.inventario import InventarioServicio  # Importa InventarioServicio
from servicio.cocina import CocinaServicio
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('merma', __name__)

trabajador_permission = Permission(RoleNeed('TRABAJADOR'))

# Mover la ruta de las mermas a un script de mermas distinto al principal
@controlador.route('/mermas',methods=['GET','POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def mermas():
    merma_servicio = MermaServicio(bd)
    mermas = merma_servicio.obtener_mermas() # Obtiene todas las mermas mediante un método del servicio
    return render_template('merma/mermas.html',mermas=mermas)

# '/agregar_merma' nombre modificado a '/merma/agregar' para seguir la convención de rutas
@controlador.route('/merma/agregar', methods=['GET', 'POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def agregar_merma():
    if request.method == 'POST':
        try:
            merma_servicio = MermaServicio(bd)
            merma_servicio.agregar_merma(request.form) # Agrega la merma mediante un método del servicio
            flash("Merma agregada exitosamente", "success")
            return redirect(url_for('principal.merma.mermas'))
        except ValueError as e:
            flash(str(e), "danger")

    insumos = InventarioServicio(bd).obtener_insumos()  # Obtiene insumos de InventarioServicio
    galletas = CocinaServicio(bd).obtener_galletas()
    producciones = CocinaServicio(bd).obtener_producciones() # Si CocinaServicio sigue gestionando producciones
    medidas = CocinaServicio(bd).obtener_medidas() # Si CocinaServicio sigue gestionando medidas
    return render_template('merma/agregar.html', insumos=insumos, galletas=galletas, producciones=producciones, medidas=medidas)