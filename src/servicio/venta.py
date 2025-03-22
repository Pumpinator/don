from modelo.venta import Venta
from modelo.venta_detalle import VentaDetalle

class VentaServicio:
    
    def __init__(self, bd):
        self.bd = bd

    def generar_venta(self, data):
        venta = Venta(
            comprador_id=data['comprador_id'],
            vendedor_id=data['vendedor_id'],
            pagado=data['pagado'],
            fecha_entrega=data['fecha_entrega']
        )
        self.bd.session.add(venta)
        self.bd.session.commit()

        for detalle in data['detalles']:
            venta_detalle = VentaDetalle(
                venta_id=venta.id,
                galleta_id=detalle['galleta_id'],
                cantidad=detalle['cantidad'],
                medida_id=detalle['medida_id']
            )
            self.bd.session.add(venta_detalle)
        
        self.bd.session.commit()