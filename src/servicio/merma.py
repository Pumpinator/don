from modelo.merma import Merma
from modelo.produccion import Produccion
class MermaServicio:
    
    def __init__ (self, bd):
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
        elif tipo == "galleta":
            merma.galleta_id = item_id
        elif tipo == "produccion":
            merma.produccion_id = item_id
            
        self.bd.session.add(merma)
        self.bd.session.commit()
        
