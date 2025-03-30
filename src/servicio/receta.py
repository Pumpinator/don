from collections import defaultdict
from sqlalchemy import func
from modelo.produccion import Produccion
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
        for nombre, galleta_nombre, cantidad, insumo_nombre, medida_nombre in resultados:
            # Si la receta ya existe en la lista, agregar el ingrediente
            receta_existente = next((r for r in recetas if r['receta'] == nombre), None)
            
            if receta_existente:
                receta_existente['ingredientes'].append({
                    'insumo': insumo_nombre,
                    'cantidad': cantidad,
                    'medida': medida_nombre
                })
            else:
                # Si no existe la receta, agregarla con los primeros ingredientes
                recetas.append({
                    'receta': nombre,
                    'galleta': galleta_nombre,
                    'ingredientes': [{
                        'insumo': insumo_nombre,
                        'cantidad': cantidad,
                        'medida': medida_nombre
                    }]
                })
        
        return recetas
