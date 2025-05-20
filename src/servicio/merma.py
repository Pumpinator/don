from modelo.merma import Merma
from modelo.produccion import Produccion
from modelo.insumo_inventario import InsumoInventario
from modelo.galleta_inventario import GalletaInventario
from modelo.receta import Receta
from sqlalchemy.orm import joinedload

class MermaServicio:

    def __init__(self, bd):
        self.bd = bd

    def obtener_mermas(self):
        return self.bd.session.query(Merma).outerjoin(Produccion).all()

    def agregar_merma(self, form):
        try:
            tipo = form.get('tipo')
            item_id = form.get('item_id')
            medida_id = form.get('medida_id')
            cantidad_str = form.get('cantidad')

            if not cantidad_str:
                raise ValueError("La cantidad es obligatoria.")

            try:
                cantidad = float(cantidad_str)
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser positiva.")
            except ValueError:
                raise ValueError("La cantidad debe ser numérica.")

            # Merma base en la medida seleccionada
            merma = Merma(
                total=cantidad,
                cantidad=cantidad,
                medida_id=medida_id
            )
#
            if tipo == "insumo":
                merma.insumo_id = item_id
                insumo = self.bd.session.query(InsumoInventario).filter_by(insumo_id=item_id).first()
                if insumo:
                    insumo.cantidad -= cantidad
                else:
                    raise ValueError(f"Insumo con ID {item_id} no encontrado en el inventario.")

            elif tipo == "galleta":
                merma.galleta_id = item_id
                galleta = self.bd.session.query(GalletaInventario).filter_by(galleta_id=item_id).first()

                if galleta:
                    # Descontar por piezas
                    galleta.cantidad -= cantidad

                    # Registrar también la merma en kilogramos
                    peso_por_pieza = 0.05  # 50 gramos = 0.05 kg
                    total_kg = cantidad * peso_por_pieza

                    merma_kilos = Merma(
                        total=total_kg,
                        cantidad=total_kg,
                        medida_id=1,  
                        galleta_id=item_id
                    )
                    self.bd.session.add(merma_kilos)
                else:
                    raise ValueError(f"Galleta con ID {item_id} no encontrada en el inventario.")

            elif tipo == "produccion":
                merma.produccion_id = item_id

                produccion = self.bd.session.query(Produccion)\
                    .options(joinedload(Produccion.receta).joinedload(Receta.galleta))\
                    .filter_by(id=item_id).first()

                if not produccion or not produccion.receta or not produccion.receta.galleta:
                    raise ValueError(f"Producción con ID {item_id} o su receta no encontrada.")

                galleta = produccion.receta.galleta
                galleta_id = galleta.id

                inventario = self.bd.session.query(GalletaInventario)\
                    .filter_by(galleta_id=galleta_id, produccion_id=item_id).first()

                if not inventario:
                    raise ValueError(f"Inventario de galleta para la producción {item_id} no encontrado.")

                # Descontar por piezas
                inventario.cantidad -= cantidad

                # Registrar también la merma en kilogramos
                peso_por_pieza = 0.05  # 50 gramos por galleta
                total_kg = cantidad * peso_por_pieza

                merma_kilos = Merma(
                    total=total_kg,
                    cantidad=total_kg,
                    medida_id=1, 
                    galleta_id=galleta_id,
                    produccion_id=item_id
                )
                self.bd.session.add(merma_kilos)

            else:
                raise ValueError(f"Tipo de merma '{tipo}' no válido.")

            
            self.bd.session.add(merma)
            self.bd.session.commit()
            return True

        except ValueError as ve:
            self.bd.session.rollback()
            print(f"Error de validación al agregar merma: {ve}")
            raise
        except Exception as e:
            self.bd.session.rollback()
            print(f"Error inesperado al agregar merma: {e}")
            raise
