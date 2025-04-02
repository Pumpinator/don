from modelo.merma import Merma
from modelo.produccion import Produccion
from modelo.insumo import Insumo
from modelo.galleta import Galleta
from modelo.insumo_inventario import InsumoInventario  # Asegúrate de importar este modelo
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
            
            # Buscar el insumo en el inventario y restarle la cantidad de la merma
            insumo_inventario = self.bd.session.query(InsumoInventario).filter_by(
                insumo_id=item_id, medida_id=medida_id
            ).first()

            if not insumo_inventario:
                raise ValueError("El insumo no se encuentra en el inventario.")
            
            if insumo_inventario.cantidad < cantidad:
                raise ValueError("No hay suficiente cantidad en el inventario para registrar esta merma.")

            insumo_inventario.cantidad -= cantidad  # Restar la merma del inventario

        elif tipo == "galleta":
            merma.galleta_id = item_id
            
            # Buscar la galleta en el inventario y restarle la cantidad de la merma
            galleta_inventario = self.bd.session.query(GalletaInventario).filter_by(
                galleta_id=item_id, medida_id=medida_id
            ).first()

            if not galleta_inventario:
                raise ValueError("La galleta no se encuentra en el inventario.")
            
            if galleta_inventario.cantidad < cantidad:
                raise ValueError("No hay suficiente cantidad en el inventario para registrar esta merma.")

            galleta_inventario.cantidad -= cantidad  # Restar la merma del inventario de galletas

        elif tipo == "produccion":
            merma.produccion_id = item_id
            # Resta cantidad de la producción si es necesario
            
        self.bd.session.add(merma)
        self.bd.session.commit()