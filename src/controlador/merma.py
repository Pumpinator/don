from flask import Blueprint, render_template, request, redirect, url_for, flash
from bd import bd
from servicio.merma import MermaServicio
from servicio.inventario import InventarioServicio  
from servicio.cocina import CocinaServicio
from flask_login import login_required
from flask_principal import Permission, RoleNeed

controlador = Blueprint('merma', __name__)

admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

# Ruta para ver todas las mermas
@controlador.route('/mermas', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def mermas():
    merma_servicio = MermaServicio(bd)
    mermas = merma_servicio.obtener_mermas()  # Obtiene todas las mermas mediante un método del servicio
    return render_template('merma/mermas.html', mermas=mermas)

# Ruta para agregar una nueva merma
@controlador.route('/merma/agregar', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def agregar_merma():
    produccion_id = request.args.get("produccion_id")
    if request.method == 'POST':
        try:
            # Agregar la merma
            merma_servicio = MermaServicio(bd)
            merma_servicio.agregar_merma(request.form)
            
            # Si se envió produccion_id en el formulario, se actualiza el estatus de la producción
            if request.form.get("produccion_id"):
                cocina_servicio = CocinaServicio(bd)
                cocina_servicio.actualizar_estatus_produccion(request.form.get("produccion_id"), 4)  # 4 = Mermado

                # Eliminar la producción del select si es mermada
                cocina_servicio.eliminar_produccion(request.form.get("produccion_id"))

                # Descontar las galletas mermadas del inventario
                galletas_merceadas = request.form.get("galletas_mermadas")
                if galletas_merceadas:
                    inventario_servicio = InventarioServicio(bd)
                    inventario_servicio.descontar_galletas_del_inventario(galletas_merceadas)

            flash("Merma agregada exitosamente", "success")
            return redirect(url_for('principal.merma.mermas'))  # Redirige a la lista de mermas

        except ValueError as e:
            flash(str(e), "danger")
            
    medidas = CocinaServicio(bd).obtener_medidas()

    # Pasa los datos necesarios a la plantilla
    insumos = InventarioServicio(bd).obtener_insumos()  
    galletas = CocinaServicio(bd).obtener_galletas()
    producciones = CocinaServicio(bd).obtener_producciones()  # Obtiene las producciones
    medidas = CocinaServicio(bd).obtener_medidas()

    # Pasa las producciones para el select en la plantilla
    return render_template('merma/agregar.html', 
                         insumos=InventarioServicio(bd).obtener_insumos(),
                         galletas=CocinaServicio(bd).obtener_galletas(),
                         producciones=CocinaServicio(bd).obtener_producciones(),
                         medidas=medidas,
                         produccion_id=produccion_id)