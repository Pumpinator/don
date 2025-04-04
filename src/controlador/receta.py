from cmath import e
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from flask_principal import Permission, RoleNeed
from flask import Blueprint, render_template, request, redirect, url_for
from bd import bd
from flask_login import login_required
from flask_principal import Permission, RoleNeed
from servicio.produccion import ProduccionServicio
from servicio.receta import RecetaServicio

controlador = Blueprint('receta', __name__)

# Permisos
admin_permission = Permission(RoleNeed('ADMIN'))
trabajador_permission = Permission(RoleNeed('TRABAJADOR'))
admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))

# Ruta para mostrar las recetas
@controlador.route('/recetas', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def recetas():
    receta = RecetaServicio(bd)
    recetas = receta.obtener_recetas()
    print(recetas)
    return render_template('receta/recetas.html', recetas=recetas)

@controlador.route('/receta/crear', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def crear_receta():
    servicio = RecetaServicio(bd)
    
    if request.method == 'GET':
        return render_template(
            'receta/crear_receta.html',
            galletas=servicio.obtener_galletas(),
            insumos=servicio.obtener_insumos(),
            medidas=servicio.obtener_medidas()
        )
    
    if request.method == 'POST':
        try:
            # Procesar datos del formulario
            ingredientes = []
            for i in range(len(request.form.getlist('insumo_id[]'))):
                ingredientes.append({
                    'insumo_id': request.form.getlist('insumo_id[]')[i],
                    'cantidad': request.form.getlist('cantidad[]')[i],
                    'medida_id': request.form.getlist('medida_id[]')[i]
                })
            
            # Crear receta
            servicio.crear_receta(
                nombre=request.form['nombre'],
                galleta_id=request.form['galleta_id'],
                procedimiento=request.form['procedimiento'],
                ingredientes=ingredientes
            )
            
            flash("Receta creada exitosamente", "success")
            return redirect(url_for('principal.receta.recetas'))
        
        except Exception as e:
            flash(f"Error al crear receta: {str(e)}", "danger")
            return redirect(url_for('principal.receta.crear_receta'))

@controlador.route('/receta/editar/<int:receta_id>', methods=['GET', 'POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def editar_receta(receta_id):
    servicio = RecetaServicio(bd) 
    
    if request.method == 'GET':
        receta = servicio.obtener_receta_por_id(receta_id)
        return render_template(
            'receta/editar_receta.html',
            receta=receta,
            galletas=servicio.obtener_galletas(),
            insumos=servicio.obtener_insumos(),
            medidas=servicio.obtener_medidas()
        )
    
    if request.method == 'POST':
        try:
            ingredientes = []
            for i in range(len(request.form.getlist('insumo_id[]'))):
                ingredientes.append({
                    'insumo_id': request.form.getlist('insumo_id[]')[i],
                    'cantidad': request.form.getlist('cantidad[]')[i],
                    'medida_id': request.form.getlist('medida_id[]')[i]
                })
            
            servicio.editar_receta( 
                receta_id=receta_id,
                nombre=request.form['nombre'],
                galleta_id=request.form['galleta_id'],
                procedimiento=request.form['procedimiento'],
                ingredientes=ingredientes
            )
            
            flash("Receta actualizada exitosamente", "success")
            return redirect(url_for('principal.receta.detalles_receta', receta_id=receta_id))
        
        except Exception as e:
            flash(f"Error al editar: {str(e)}", "danger")
            return redirect(url_for('principal.receta.editar_receta', receta_id=receta_id))
        
@controlador.route('/receta/hornear', methods=['POST'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def hornear_receta():
    try:
        receta_id = request.form['receta_id']
        kilos = float(request.form['kilos'])
        
        produccion_servicio = ProduccionServicio(bd)
        produccion = produccion_servicio.crear_produccion(
            receta_id=receta_id,
            fecha=datetime.now().date(),
            kilos=kilos
        )
        
        flash("Producción iniciada exitosamente", "success")
    except Exception as e:
        flash(f"Error al hornear: {str(e)}", "danger")
    
    return redirect(url_for('principal.receta.recetas'))

@controlador.route('/receta/detalles/<int:receta_id>', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def detalles_receta(receta_id):
    try:
        servicio = RecetaServicio(bd)
        receta = servicio.obtener_receta_por_id(receta_id)
        return render_template('receta/detalles_receta.html', receta=receta)
    except Exception as e:
        flash(f"Error al cargar los detalles de la receta: {str(e)}", "danger")
        return redirect(url_for('principal.receta.recetas'))

@controlador.route('/receta/eliminar/<int:receta_id>', methods=['POST'])
@login_required
@trabajador_permission.require(http_exception=403)
def eliminar_receta(receta_id):
    try:
        servicio = RecetaServicio(bd)
        servicio.eliminar_receta(receta_id)
        flash("Receta eliminada exitosamente", "success")
    except Exception as e:
        error_msg = str(e)
        if "producciones registradas" in error_msg:
            flash(f"{error_msg}", "warning")
        else:
            flash(f"{error_msg}", "danger")
    
    return redirect(url_for('principal.receta.recetas'))