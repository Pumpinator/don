from modelo.galleta import Galleta
from modelo.medida import Medida
from modelo.insumo import Insumo
from modelo.insumo_inventario import InsumoInventario
from modelo.galleta_inventario import GalletaInventario
from sqlalchemy import func

class InventarioServicio:
    def __init__ (self, bd):
        self.bd = bd
        
    def obtener_galleta(self, id):
        return self.bd.session.query(Galleta).get(id)

    def obtener_galletas(self):
        resultados = (
            self.bd.session
            .query(
                Galleta.nombre, 
                func.sum(GalletaInventario.cantidad),
                Medida.nombre
            )
            .join(Galleta, Galleta.id == GalletaInventario.galleta_id)
            .join(Medida, GalletaInventario.medida_id == Medida.id)
            .group_by(Galleta.nombre, Medida.nombre)
            .all()
        )
        inventarios = [
            {"galleta": nombre, "cantidad": int(total), "medida": medida} 
            for nombre, total, medida in resultados
        ]
        return inventarios
    

    def obtener_insumos(self):
        return self.bd.session.query(Insumo).all()
    
    def obtener_insumo(self, id):
        return self.bd.session.query(Insumo).filter(Insumo.id == id).first()
    

    def obtener_detalles_insumo(self, insumo_id):
        insumos = (
            self.bd.session.query(
                Insumo.nombre, 
                InsumoInventario.cantidad,
                Medida.nombre,
                InsumoInventario.fecha_expiracion
            )
            .join(Insumo, Insumo.id == InsumoInventario.insumo_id)
            .join(Medida, InsumoInventario.medida_id == Medida.id)
            .filter(InsumoInventario.insumo_id == insumo_id)  # Aplica el filtro aquí
            .group_by(InsumoInventario.cantidad, Insumo.nombre, Medida.nombre, InsumoInventario.fecha_expiracion)
            .all()
        )
        inventarios = [
            {"insumo": nombre, "cantidad": int(total), "medida": medida, "caducidad": fecha_expiracion} 
            for nombre, total, medida, fecha_expiracion in insumos
        ]
        return inventarios

    def obtener_insumos_inventarios(self):
        resultados = (
            self.bd.session
            .query(
                InsumoInventario.insumo_id,
                Insumo.nombre, 
                func.sum(InsumoInventario.cantidad),
                Medida.nombre
            )
            .join(Insumo, Insumo.id == InsumoInventario.insumo_id)
            .join(Medida, InsumoInventario.medida_id == Medida.id)
            .group_by(InsumoInventario.insumo_id, Insumo.nombre, Medida.nombre)
            .all()
        )
        inventarios = [
            {"insumo_id": insumo_id, "insumo": nombre, "cantidad": int(total), "medida": medida} 
            for insumo_id, nombre, total, medida in resultados
        ]
        return inventarios