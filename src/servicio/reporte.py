from modelo.venta import Venta
from modelo.venta_detalle import VentaDetalle
from modelo.compra import Compra
from modelo.compra_detalle import CompraDetalle
from bd import bd
from modelo.galleta import Galleta
from modelo.medida import Medida


class ReporteVentas:

    def __init__(self):
        self.bd = bd  

    def obtener_mas_vendidos(self):
        productos_mas_vendidos = (
            self.bd.session.query(
                Galleta.nombre, 
                Medida.nombre.label('medida_mas_vendida'),  # Agregar la medida
                self.bd.func.sum(VentaDetalle.cantidad).label('total_vendido')
            )
            .join(VentaDetalle, Galleta.id == VentaDetalle.galleta_id)
            .join(Medida, Galleta.medida_id == Medida.id)  # Unir con la tabla de medida
            .group_by(Galleta.nombre, Medida.nombre)  # Agrupar también por la medida
            .order_by(self.bd.desc('total_vendido'))
            .limit(10)
            .all()
        )

        return productos_mas_vendidos
    
    def obtener_resumen(self):
        #Obtiene un resumen de las ventas y los gastos.
        resumen_ventas = (
            self.bd.session.query(
                Venta.fecha_entrega, 
                self.bd.func.count(Venta.id).label('total_ventas'),
                self.bd.func.sum(VentaDetalle.cantidad).label('total_galletas_vendidas'),
                self.bd.func.sum(VentaDetalle.cantidad * VentaDetalle.precio_unitario).label('ingresos_totales')
            )
            .join(VentaDetalle, Venta.id == VentaDetalle.venta_id)
            .group_by(Venta.fecha_entrega)
            .all()
        )

        resumen_gastos = (
            self.bd.session.query(
                Compra.fecha, 
                self.bd.func.sum(CompraDetalle.cantidad * CompraDetalle.precio_unitario).label('total_gastos')
            )
            .join(CompraDetalle, Compra.id == CompraDetalle.compra_id)
            .group_by(Compra.fecha)
            .all()
        )
        resumen_ventas_dict = {rv[0]: {'total_ventas': rv[1], 'total_galletas_vendidas': rv[2], 'ingresos_totales': rv[3]} for rv in resumen_ventas}
        resumen_gastos_dict = {rg[0]: {'total_gastos': rg[1]} for rg in resumen_gastos}
        resumen_final = []
        fechas = set(resumen_ventas_dict.keys()).union(set(resumen_gastos_dict.keys()))

        for fecha in fechas:
            total_ventas = resumen_ventas_dict.get(fecha, {}).get('total_ventas', 0)
            total_galletas_vendidas = resumen_ventas_dict.get(fecha, {}).get('total_galletas_vendidas', 0)
            ingresos_totales = resumen_ventas_dict.get(fecha, {}).get('ingresos_totales', 0)
            total_gastos = resumen_gastos_dict.get(fecha, {}).get('total_gastos', 0)

            resumen_final.append({
                'fecha': fecha,
                'total_ventas': total_ventas,
                'total_galletas_vendidas': total_galletas_vendidas,
                'ingresos_totales': ingresos_totales,
                'total_gastos': total_gastos,
                'ganancias': ingresos_totales - total_gastos 
            })
        return resumen_final
