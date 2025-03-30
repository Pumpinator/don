from modelo.proveedor import Proveedor

class ProveedorServicio:
    def __init__(self, bd):
        self.bd = bd
        
    def obtener_proveedores(self):
        return self.bd.session.query(Proveedor).all()
    
    def obtener_proveedor_por_id(self, proveedor_id):
        return self.bd.session.query(Proveedor).get(proveedor_id)
    
    def crear_proveedor(self, nombre, contacto):
        try:
            nuevo_proveedor = Proveedor(nombre=nombre, contacto=contacto)
            self.bd.session.add(nuevo_proveedor)
            self.bd.session.commit()
            return nuevo_proveedor
        except Exception as e:
            self.bd.session.rollback()
            raise e
    
    def editar_proveedor(self, proveedor_id, nombre, contacto):
        try:
            proveedor = self.obtener_proveedor_por_id(proveedor_id)
            proveedor.nombre = nombre
            proveedor.contacto = contacto
            self.bd.session.commit()
            return proveedor
        except Exception as e:
            self.bd.session.rollback()
            raise e
    
    def eliminar_proveedor(self, proveedor_id):
        try:
            proveedor = self.obtener_proveedor_por_id(proveedor_id)
            if proveedor:
                self.bd.session.delete(proveedor)
                self.bd.session.commit()
            return True
        except Exception as e:
            self.bd.session.rollback()
            raise e