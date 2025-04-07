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
            cantidad = form.get('cantidad')

            if not cantidad:
                raise ValueError("La cantidad es obligatoria.")
            try:
                cantidad = float(cantidad)
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser positiva.")
            except ValueError:
                raise ValueError("La cantidad debe ser numérica.")

            merma = Merma(total=cantidad, cantidad=cantidad, medida_id=medida_id)

            if tipo == "insumo":
                merma.insumo_id = item_id
                insumo = self.bd.session.query(InsumoInventario).filter_by(insumo_id=item_id).first()
                if insumo:
                    insumo.cantidad -= cantidad
            elif tipo == "galleta":
                merma.galleta_id = item_id
                galleta = self.bd.session.query(GalletaInventario).filter_by(galleta_id=item_id).first()
                if galleta:
                    galleta.cantidad -= cantidad
            elif tipo == "produccion":
                merma.produccion_id = item_id

                # Obtener la producción y su receta
                produccion = self.bd.session.query(Produccion)\
                    .options(joinedload(Produccion.receta).joinedload(Receta.galleta))\
                    .filter_by(id=item_id).first()

                if not produccion:
                    raise ValueError("Producción no encontrada.")
                if not produccion.receta or not produccion.receta.galleta:
                    raise ValueError("La producción no tiene una receta o galleta asociada.")

                galleta_id = produccion.receta.galleta.id
                inventario = self.bd.session.query(GalletaInventario).filter_by(galleta_id=galleta_id).first()

                if not inventario:
                    raise ValueError("Inventario de galleta no encontrado.")

                # Descontar del inventario de galleta
                inventario.cantidad -= cantidad
                

            else:
                raise ValueError("Tipo de merma no válido.")

            self.bd.session.add(merma)
            self.bd.session.commit()
            return True

        except Exception as e:
            self.bd.session.rollback()
            print(f"Error al agregar merma: {e}")
            raise
