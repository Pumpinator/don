from flask import Blueprint, render_template, request, redirect, url_for, flash
from bd import bd
from servicio.merma import MermaServicio
from servicio.cocina import CocinaServicio
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('merma', __name__)

admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
comprador_permission = Permission(RoleNeed('COMPRADOR'))

# Mover la ruta de las mermas a un script de mermas distinto al principal
@controlador.route('/mermas',methods=['GET','POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def mermas():
    merma_servicio = MermaServicio(bd)
    mermas = merma_servicio.obtener_mermas() # Obtiene todas las mermas mediante un método del servicio
    return render_template('mermas.html')


@controlador.route('/agregar_merma', methods=['GET', 'POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def agregar_merma():
    cocina_servicio = CocinaServicio(bd)
    if request.method == 'POST':
        try:
            merma_servicio = MermaServicio(bd)
            merma_servicio.agregar_merma(request.form) # Agrega la merma mediante un método del servicio
            flash("Merma agregada exitosamente", "success")
        except ValueError as e:
            flash(str(e), "danger")

        return redirect(url_for('principal.mermas'))

    insumos = cocina_servicio.obtener_insumos()
    galletas = cocina_servicio.obtener_galletas()
    producciones = cocina_servicio.obtener_producciones()
    medidas = cocina_servicio.obtener_medidas()
    return render_template('agregar_merma.html', insumos=insumos, galletas=galletas, producciones=producciones, medidas=medidas)
