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
        return self.bd.session.query(Galleta).all()
    
    def detalles_galleta(self, galleta_id):
        galletas = (
            self.bd.session.query(
                Galleta.nombre, 
                GalletaInventario.cantidad,
                GalletaInventario.fecha_expiracion
            )
            .join(Galleta, Galleta.id == GalletaInventario.galleta_id)
            .filter(GalletaInventario.galleta_id == galleta_id)  
            .group_by(GalletaInventario.cantidad, Galleta.nombre, GalletaInventario.fecha_expiracion)
            .all()
        )
        inventarios = [
            {"galleta": nombre, "cantidad": int(total),  "caducidad": fecha_expiracion} 
            for nombre, total,  fecha_expiracion in galletas
        ]
        return inventarios
    

    def obtener_galletas_inv(self):
        resultados = (
            self.bd.session
            .query(
                Galleta.id,
                Galleta.nombre, 
                Galleta.imagen,
                func.sum(GalletaInventario.cantidad).label("cantidad_total"),
                Medida.nombre
            )
            .join(Galleta, Galleta.id == GalletaInventario.galleta_id)
            .join(Medida, GalletaInventario.medida_id == Medida.id)
            .group_by(Galleta.id, Galleta.nombre, Galleta.imagen, Medida.nombre)
            .all()
        )
        inventarios = [
            {
                "id": galleta_id,
                "imagen": imagen,
                "galleta": nombre,
                "cantidad_kg": float(cantidad_total),
                "cantidad_piezas": int(cantidad_total / 0.05),  # Convertir a piezas
                "medida": medida
            }
            for galleta_id, nombre, imagen, cantidad_total, medida in resultados
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
            .filter(InsumoInventario.insumo_id == insumo_id)  
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
                Insumo.id,
                Insumo.nombre, 
                func.sum(InsumoInventario.cantidad).label("cantidad_total"),
                Medida.nombre
            )
            .join(Insumo, Insumo.id == InsumoInventario.insumo_id)
            .join(Medida, InsumoInventario.medida_id == Medida.id)
            .group_by(Insumo.id,Insumo.nombre, Medida.nombre)
            .all()
        )
        inventarios = [
            {"id":insumo_id,"insumo": nombre, "cantidad": int(cantidad_total), "medida": medida} 
            for insumo_id, nombre, cantidad_total, medida in resultados
        ]
        return inventarios
    
    def editar_insumo(self, form, insumo_id):
        # Verificar si el insumo existe
        insumo = self.bd.session.query(Insumo).filter_by(id=insumo_id).first()
        if not insumo:
            raise ValueError("Insumo not found")
        
        # Verificar si ya existe otro insumo con el mismo nombre
        nombre_existente = self.bd.session.query(Insumo).filter(Insumo.nombre == form.nombre.data, Insumo.id != insumo_id).first()
        if nombre_existente:
            raise ValueError(f"Ya existe un insumo con el nombre '{form.nombre.data}'")
        
        # Actualizar el insumo con los datos del formulario
        insumo.nombre = form.nombre.data
        insumo.cantidad = form.cantidad.data
        self.bd.session.commit()