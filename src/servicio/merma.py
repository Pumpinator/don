from modelo.merma import Merma
from modelo.produccion import Produccion
from modelo.insumo_inventario import InsumoInventario
from modelo.galleta_inventario import GalletaInventario

class MermaServicio:

    def __init__(self, bd):
        self.bd = bd

    def obtener_mermas(self):
        return self.bd.session.query(Merma).outerjoin(Produccion).all()

    def agregar_merma(self, form):
        tipo = form.get('tipo')
        item_id = form.get('item_id')
        medida_id = form.get('medida_id')
        cantidad = form.get('cantidad')

        if not cantidad:
            raise ValueError("La cantidad es obligatoria.")

        try:
            cantidad = float(cantidad)
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un número positivo.")
        except ValueError:
            raise ValueError("La cantidad debe ser un número válido.")

        merma = Merma(total=cantidad, cantidad=cantidad, medida_id=medida_id)

        if tipo == "insumo":
            merma.insumo_id = item_id

            insumo_inventario = self.bd.session.query(InsumoInventario).filter_by(
                insumo_id=item_id, medida_id=medida_id
            ).first()

            if not insumo_inventario:
                raise ValueError("El insumo no se encuentra en el inventario.")

            if insumo_inventario.cantidad < cantidad:
                raise ValueError("No hay suficiente cantidad en el inventario para registrar esta merma.")

            insumo_inventario.cantidad -= cantidad

        elif tipo == "galleta":
            merma.galleta_id = item_id

            galleta_inventario = self.bd.session.query(GalletaInventario).filter_by(
                galleta_id=item_id, medida_id=medida_id
            ).first()

            if not galleta_inventario:
                raise ValueError("La galleta no se encuentra en el inventario.")

            if galleta_inventario.cantidad < cantidad:
                raise ValueError("No hay suficiente cantidad en el inventario para registrar esta merma.")

            galleta_inventario.cantidad -= cantidad

        elif tipo == "produccion":
            merma.produccion_id = item_id
            produccion = self.bd.session.query(Produccion).filter_by(id=item_id).first()

            if not produccion:
                raise ValueError("La producción no existe.")
            
            merma.produccion = produccion  # Asigna el objeto completo si es necesario

            # Actualiza el estatus antes de guardar la merma
            produccion.estatus = 4  # Asegúrate de que el estatus esté siendo correctamente asignado.

        self.bd.session.flush()  # Fuerza la actualización de los cambios pendientes
        self.bd.session.add(merma)
        self.bd.session.commit()
