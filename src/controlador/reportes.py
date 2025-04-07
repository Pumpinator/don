from flask_login import login_required
from flask_principal import Permission, RoleNeed
from servicio.reporte import ReporteVentas
from bd import bd
from flask import Blueprint, render_template, request

controlador = Blueprint('reportes', __name__)
admin_or_trabajador_permission = Permission(RoleNeed('ADMIN'), RoleNeed('TRABAJADOR'))


@controlador.route('/reportes', methods=['GET'])
@login_required
@admin_or_trabajador_permission.require(http_exception=403)
def reportes():
    periodo = request.args.get('periodo', 'mensual')  # Obtener el periodo seleccionado (default: mensual)
    
    reporte_ventas = ReporteVentas()  
    resumen_ventas = reporte_ventas.obtener_resumen(periodo)
    productos_mas_vendidos = reporte_ventas.obtener_mas_vendidos(periodo)

    return render_template(
        'reportes.html', 
        resumen_ventas=resumen_ventas, 
        productos_mas_vendidos=productos_mas_vendidos,
        periodo_seleccionado=periodo
    )