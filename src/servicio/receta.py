from sqlalchemy.orm import joinedload
from modelo.produccion import Produccion
from modelo.receta import Receta
from modelo.ingrediente import Ingrediente
from modelo.galleta import Galleta
from modelo.insumo import Insumo
from modelo.medida import Medida

class RecetaServicio:
    def __init__(self, bd):
        self.bd = bd

    def obtener_recetas(self):
        resultados = (
            self.bd.session.query(
                Receta.id,
                Receta.nombre,
                Receta.procedimiento,
                Galleta.nombre.label('galleta_nombre'),
                Galleta.imagen.label('galleta_imagen'),
                Insumo.nombre.label('insumo_nombre'),
                Ingrediente.cantidad,
                Medida.abreviatura.label('medida_nombre')
            )
            .join(Receta.galleta)
            .join(Ingrediente, Receta.id == Ingrediente.receta_id)
            .join(Insumo, Ingrediente.insumo_id == Insumo.id)
            .join(Medida, Ingrediente.medida_id == Medida.id)
            .order_by(Receta.nombre)
            .all()
        )

        recetas_dict = {}
        for row in resultados:
            receta_id = row.id
            
            if receta_id not in recetas_dict:
                recetas_dict[receta_id] = {
                    'id': receta_id,
                    'nombre': row.nombre,
                    'procedimiento': row.procedimiento,
                    'galleta': row.galleta_nombre,
                    'imagen': row.galleta_imagen,
                    'ingredientes': []
                }
            
            recetas_dict[receta_id]['ingredientes'].append({
                'insumo': row.insumo_nombre,
                'cantidad': row.cantidad,
                'medida': row.medida_nombre
            })

        return list(recetas_dict.values())

    def obtener_galletas(self):
        return self.bd.session.query(Galleta).all()

    def obtener_insumos(self):
        return self.bd.session.query(Insumo).all()

    def obtener_medidas(self):
        return self.bd.session.query(Medida).all()

    def crear_receta(self, nombre, galleta_id, procedimiento, ingredientes):
        try:
            # Crear la receta
            nueva_receta = Receta(
                nombre=nombre,
                galleta_id=galleta_id,
                procedimiento=procedimiento
            )
            self.bd.session.add(nueva_receta)
            self.bd.session.flush()  # Para obtener el ID de la nueva receta

            # Crear los ingredientes
            for insumo in ingredientes:
                nuevo_ingrediente = Ingrediente(
                    receta_id=nueva_receta.id,
                    insumo_id=insumo['insumo_id'],
                    cantidad=insumo['cantidad'],
                    medida_id=insumo['medida_id']
                )
                self.bd.session.add(nuevo_ingrediente)

            self.bd.session.commit()
            return nueva_receta
        except Exception as e:
            self.bd.session.rollback()
            raise e

    def editar_receta(self, receta_id, nombre, galleta_id, procedimiento, ingredientes):
        try:
            # Actualizar receta
            receta = self.bd.session.query(Receta).get(receta_id)
            receta.nombre = nombre
            receta.galleta_id = galleta_id
            receta.procedimiento = procedimiento

            # Eliminar ingredientes antiguos
            self.bd.session.query(Ingrediente).filter_by(receta_id=receta_id).delete()

            # Crear nuevos ingredientes
            for insumo in ingredientes:
                nuevo_ingrediente = Ingrediente(
                    receta_id=receta_id,
                    insumo_id=insumo['insumo_id'],
                    cantidad=insumo['cantidad'],
                    medida_id=insumo['medida_id']
                )
                self.bd.session.add(nuevo_ingrediente)

            self.bd.session.commit()
            return receta
        except Exception as e:
            self.bd.session.rollback()
            raise e

    def obtener_receta_por_id(self, receta_id):
        try:
            receta = (
                self.bd.session.query(
                    Receta.id,
                    Receta.nombre,
                    Receta.procedimiento,
                    Galleta.nombre.label('galleta_nombre'),
                    Ingrediente.cantidad,
                    Ingrediente.insumo_id,
                    Insumo.nombre.label('insumo_nombre'),
                    Medida.nombre.label('medida_nombre')
                )
                .join(Receta.galleta)
                .join(Ingrediente, Receta.id == Ingrediente.receta_id)
                .join(Insumo, Ingrediente.insumo_id == Insumo.id)
                .join(Medida, Ingrediente.medida_id == Medida.id)
                .filter(Receta.id == receta_id)
                .all()
            )

            if not receta:
                raise Exception("Receta no encontrada")

            receta_dict = {
                'id': receta[0].id,
                'nombre': receta[0].nombre,
                'procedimiento': receta[0].procedimiento,
                'galleta': receta[0].galleta_nombre,
                'ingredientes': []
            }

            for row in receta:
                receta_dict['ingredientes'].append({
                    'insumo': row.insumo_nombre,
                    'cantidad': row.cantidad,
                    'medida': row.medida_nombre,
                    'insumo_id': row.insumo_id
                })

            return receta_dict
        except Exception as e:
            raise e
    
    def eliminar_receta(self, receta_id):
        try:
            producciones_invalidas = self.bd.session.query(Produccion).filter(
                Produccion.receta_id == receta_id,
                Produccion.estatus != 4
            ).count()
            
            if producciones_invalidas > 0:
                raise ValueError("No se puede eliminar: existen producciones activas o en proceso")

            # Eliminar producciones con estatus 4 (si existen)
            self.bd.session.query(Produccion).filter(
                Produccion.receta_id == receta_id,
                Produccion.estatus == 4
            ).delete()

            # Eliminar ingredientes
            self.bd.session.query(Ingrediente).filter_by(receta_id=receta_id).delete()
            
            # Eliminar la receta
            receta = self.bd.session.query(Receta).get(receta_id)
            if receta:
                self.bd.session.delete(receta)
                
            self.bd.session.commit()
            return True
        except Exception as e:
            self.bd.session.rollback()
            raise e