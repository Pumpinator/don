from sqlalchemy import text
from modelo.receta import Receta
from modelo.ingrediente import Ingrediente
from modelo.insumo import Insumo
from modelo.galleta import Galleta
from modelo.medida import Medida

class RecetaServicio:
    def __init__(self, bd):
        self.bd = bd

def obtener_recetas(self):
    resultados = (
        self.bd.session
        .query(
            Receta.nombre,
            Receta.procedimiento,
            Galleta.nombre.label('galleta_nombre'),
            Ingrediente.cantidad,
            Insumo.nombre.label('insumo_nombre'),
            Medida.nombre.label('medida_nombre')
        )
        .join(Receta.galleta)
        .join(Ingrediente, Ingrediente.receta_id == Receta.id)
        .join(Insumo, Insumo.id == Ingrediente.insumo_id)  
        .join(Medida, Medida.id == Ingrediente.medida_id)
        .all()
    )
    
    recetas = []
    for nombre, procedimiento, galleta_nombre, cantidad, insumo_nombre, medida_nombre in resultados:
        receta_existente = next((r for r in recetas if r['receta'] == nombre), None)
        
        if receta_existente:
            receta_existente['ingredientes'].append({
                'insumo': insumo_nombre,
                'cantidad': cantidad,
                'medida': medida_nombre
            })
        else:
            recetas.append({
                'receta': nombre,
                'procedimiento': procedimiento,
                'galleta': galleta_nombre,
                'ingredientes': [{
                    'insumo': insumo_nombre,
                    'cantidad': cantidad,
                    'medida': medida_nombre
                }]
            })
    
    return recetas

    def crear_receta(self, nombre, galleta_id, procedimiento, insumo_ids, cantidades, medida_ids):
        try:
            insumos_str = ','.join(insumo_ids)
            cantidades_str = ','.join(cantidades)
            medidas_str = ','.join(medida_ids)

            query = text("CALL SP_InsertarReceta(:nombre, :galleta_id, :procedimiento, :insumos, :cantidades, :medidas)")
            self.bd.session.execute(query, {
                'nombre': nombre,
                'galleta_id': galleta_id,
                'procedimiento': procedimiento,
                'insumos': insumos_str,
                'cantidades': cantidades_str,
                'medidas': medidas_str
            })

            self.bd.session.commit()

        except Exception as e:
            self.bd.session.rollback()
            raise e

    def editar_receta(self, receta_id, nombre, galleta_id, procedimiento, insumo_ids, cantidades, medida_ids):
        try:
            receta = self.bd.session.query(Receta).filter(Receta.id == receta_id).first()

            if not receta:
                raise ValueError("Receta no encontrada")

            receta.nombre = nombre
            receta.galleta_id = galleta_id
            receta.procedimiento = procedimiento
            self.bd.session.commit()

            self.bd.session.query(Ingrediente).filter(Ingrediente.receta_id == receta_id).delete()

            for insumo_id, cantidad, medida_id in zip(insumo_ids, cantidades, medida_ids):
                ingrediente = Ingrediente(
                    receta_id=receta.id,
                    insumo_id=insumo_id,
                    cantidad=cantidad,
                    medida_id=medida_id
                )
                self.bd.session.add(ingrediente)

            self.bd.session.commit()

        except Exception as e:
            self.bd.session.rollback()
            raise e
