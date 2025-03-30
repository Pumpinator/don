from modelo.compra import Compra
from modelo.proveedor import Proveedor
from modelo.compra_detalle import CompraDetalle

class CompraServicio:
    
    def __init__(self, bd):
        self.bd = bd
        
    def obtener_compras(self):
        return self.bd.session.query(Compra).all()
    
    def obtener_compra(self, compra_id):
        return self.bd.session.query(Compra).get(compra_id)
    
    def obtener_compra_detalles(self, compra_id):
        return self.bd.session.query(CompraDetalle).filter(CompraDetalle.compra_id == compra_id).all()
    
    def obtener_proveedores(self):
        return self.bd.session.query(Proveedor).all()
    
    def obtener_proveedor(self, proveedor_id):
        return self.bd.session.query(Proveedor).get(proveedor_id)
    
    def crear_compra(self, compra):
        self.bd.session.add(compra)
        self.bd.session.commit()
        return compra
    
    