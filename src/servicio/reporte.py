from modelo.venta import Venta
from modelo.venta_detalle import VentaDetalle
from modelo.compra import Compra
from modelo.compra_detalle import CompraDetalle
from bd import bd
from modelo.galleta import Galleta
from modelo.medida import Medida
from modelo.galleta_inventario import GalletaInventario 
from datetime import datetime, timedelta

class ReporteVentas:

    def __init__(self):
        self.bd = bd  

    def obtener_mas_vendidos(self, periodo='mensual'):
        query = (
            self.bd.session.query(
                Galleta.nombre, 
                Medida.nombre.label('medida_mas_vendida'),
                VentaDetalle.presentacion.label('presentacion_mas_vendida'),
                self.bd.func.sum(VentaDetalle.cantidad).label('total_vendido')
            )
            .join(VentaDetalle, Galleta.id == VentaDetalle.galleta_id)
            .join(GalletaInventario, Galleta.id == GalletaInventario.galleta_id)
            .join(Medida, GalletaInventario.medida_id == Medida.id)
            .join(Venta, VentaDetalle.venta_id == Venta.id)
        )
        
        # Filtrar por periodo
        if periodo == 'diario':
            hoy = datetime.now().date()
            query = query.filter(self.bd.func.date(Venta.fecha) == hoy)
        elif periodo == 'mensual':
            hoy = datetime.now().date()
            primer_dia_mes = hoy.replace(day=1)
            query = query.filter(self.bd.func.date(Venta.fecha) >= primer_dia_mes)
            
        productos_mas_vendidos = (
            query.group_by(Galleta.nombre, Medida.nombre, VentaDetalle.presentacion)
            .order_by(self.bd.desc('total_vendido'))
            .limit(10)
            .all()
        )

        return productos_mas_vendidos
    
    def obtener_resumen(self, periodo='mensual'):
        # Consulta para ventas
        ventas_query = (
            self.bd.session.query(
                self.bd.func.count(Venta.id).label('total_ventas'),
                self.bd.func.sum(VentaDetalle.cantidad).label('total_galletas_vendidas'),
                self.bd.func.sum(VentaDetalle.cantidad * VentaDetalle.precio_unitario).label('ingresos_totales')
            )
            .join(VentaDetalle, Venta.id == VentaDetalle.venta_id)
        )
        
        # Consulta para gastos
        gastos_query = (
            self.bd.session.query(
                self.bd.func.sum(CompraDetalle.cantidad * CompraDetalle.precio_unitario).label('total_gastos')
            )
            .select_from(Compra)  
            .join(CompraDetalle, Compra.id == CompraDetalle.compra_id)
        )
        
        # Filtrar por periodo
        if periodo == 'diario':
            hoy = datetime.now().date()
            ventas_query = ventas_query.filter(self.bd.func.date(Venta.fecha) == hoy)
            gastos_query = gastos_query.filter(self.bd.func.date(Compra.fecha) == hoy)
        elif periodo == 'mensual':
            hoy = datetime.now().date()
            primer_dia_mes = hoy.replace(day=1)
            ventas_query = ventas_query.filter(self.bd.func.date(Venta.fecha) >= primer_dia_mes)
            gastos_query = gastos_query.filter(self.bd.func.date(Compra.fecha) >= primer_dia_mes)
        
        resumen_ventas = ventas_query.first()
        resumen_gastos = gastos_query.scalar()

        # Si no hay ventas, establecer valores por defecto
        if resumen_ventas[2] is None:  
            resumen_ventas = (0, 0, 0)
        
        if resumen_gastos is None:
            resumen_gastos = 0

        return [{
            'total_ventas': resumen_ventas[0],
            'total_galletas_vendidas': resumen_ventas[1],
            'ingresos_totales': resumen_ventas[2],
            'total_gastos': resumen_gastos,
            'ganancias': resumen_ventas[2] - resumen_gastos
        }]