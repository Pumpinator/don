from modelo.venta import Venta
from modelo.venta_detalle import VentaDetalle
from modelo.galleta import Galleta
from sqlalchemy import func, extract
from datetime import datetime, timedelta
class ReporteVentas:
    @staticmethod
    def obtener_resumen():
        """
        Obtiene un resumen de las ventas, agrupadas por fecha.
        """
        from modelo.venta import Venta
        from modelo.venta_detalle import VentaDetalle
        from bd import bd
        
        resumen = (
            bd.session.query(
                Venta.fecha_entrega, 
                bd.func.count(Venta.id).label('total_ventas'),
                bd.func.sum(VentaDetalle.cantidad).label('total_galletas_vendidas')
            )
            .join(VentaDetalle, Venta.id == VentaDetalle.venta_id)
            .group_by(Venta.fecha_entrega)
            .all()
        )
        
        return resumen

    @staticmethod
    def obtener_mas_vendidos():
        """
        Obtiene las galletas más vendidas.
        """
        from modelo.galleta import Galleta
        from modelo.venta_detalle import VentaDetalle
        from bd import bd

        productos_mas_vendidos = (
            bd.session.query(
                Galleta.nombre, 
                bd.func.sum(VentaDetalle.cantidad).label('total_vendido')
            )
            .join(VentaDetalle, Galleta.id == VentaDetalle.galleta_id)
            .group_by(Galleta.nombre)
            .order_by(bd.desc('total_vendido'))
            .limit(10)
            .all()
        )

        return productos_mas_vendidos
