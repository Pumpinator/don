from modelo.venta import Venta
from modelo.venta_detalle import VentaDetalle
from bd import bd

def generar_venta(data):
    venta = Venta(
        comprador_id=data['comprador_id'],
        vendedor_id=data['vendedor_id'],
        pagado=data['pagado'],
        fecha_entrega=data['fecha_entrega']
    )
    bd.session.add(venta)
    bd.session.commit()

    for detalle in data['detalles']:
        venta_detalle = VentaDetalle(
            venta_id=venta.id,
            galleta_id=detalle['galleta_id'],
            cantidad=detalle['cantidad'],
            medida_id=detalle['medida_id']
        )
        bd.session.add(venta_detalle)
    
    bd.session.commit()