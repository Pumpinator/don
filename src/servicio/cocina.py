from modelo.medida import Medida
from modelo.insumo import Insumo
from modelo.insumo_inventario import InsumoInventario
from modelo.galleta import Galleta
from modelo.produccion import Produccion
from sqlalchemy import func

class CocinaServicio:
    
    def __init__ (self, bd):
        self.bd=bd
        
    def obtener_insumos(self):
        resultados = (
            self.bd.session.query(
                Insumo.nombre,
                func.sum(InsumoInventario.cantidad).label("cantidad_total"),
                InsumoInventario.medida
            )
            .join(Insumo, Insumo.id == InsumoInventario.insumo_id)
            .join(Medida, InsumoInventario.medida_id == Medida.id)
            .group_by(Insumo.nombre, InsumoInventario.medida)
            .all()
        )
        inventarios = [
            {"insumo": nombre, "cantidad": int(cantidad_total), "medida": medida} 
            for nombre, cantidad_total, medida in resultados
        ]
        return inventarios
    
    def obtener_medidas(self):
        return self.bd.session.query(Medida).distinct().all()
    
    def obtener_producciones(self):
        estatus_dict = {
        1: "🛠 Haciendo",
        2: "🔥 Cocinando",
        3: "✅ Listo",
        4: "❌ Mermado"  # Agregado para marcar las producciones mermadas
    }
        producciones = self.bd.session.query(Produccion).all()
    
    # Filtra producciones con estatus "Mermado"
        producciones = [p for p in producciones if p.estatus != 4]
    
        for produccion in producciones:
            produccion.descripcion_estatus = estatus_dict.get(produccion.estatus, "Desconocido")

        return producciones
    
    def obtener_galletas(self):
        return self.bd.session.query(Galleta).all()
    
    def agregar_galletas(self, form):
        nombre = form.get('nombre')
        precio = form.get('precio')
    
        
        # Verificar si ya existe una galleta con el mismo nombre
        galleta_existente = self.bd.session.query(Galleta).filter_by(nombre=nombre).first()
        if galleta_existente:
            raise ValueError(f"Ya existe una galleta con el nombre '{nombre}'")
        
        # Agregar la nueva galleta si no existe
        galleta = Galleta(nombre=nombre, precio=precio)
        self.bd.session.add(galleta)
        self.bd.session.commit()

    def editar_galleta(self, form):
        id = form.get('id')
        nombre = form.get('nombre')
        precio = form.get('precio')
        
        # Verificar si ya existe una galleta con el mismo nombre (excluyendo la actual)
        galleta_existente = self.bd.session.query(Galleta).filter(
            Galleta.nombre == nombre,
            Galleta.id != id
        ).first()
        
        if galleta_existente:
            raise ValueError(f"Ya existe una galleta con el nombre '{nombre}'")
        
        # Actualizar la galleta si no existe otra con el mismo nombre
        galleta = self.bd.session.query(Galleta).filter_by(id=id).first()
        if galleta:
            galleta.nombre = nombre
            galleta.precio = precio
            self.bd.session.commit()
        else:
            raise ValueError(f"Galleta con ID '{id}' no encontrada")


    def agregar_insumo(self, form):
        nombre = form.get('nombre')
        
        # Verificar si ya existe un insumo con el mismo nombre
        insumo_existente = self.bd.session.query(Insumo).filter_by(nombre=nombre).first()
        if insumo_existente:
            raise ValueError(f"Ya existe un insumo con el nombre '{nombre}'")
        
        # Agregar el nuevo insumo si no existe
        insumo = Insumo(nombre=nombre)
        self.bd.session.add(insumo)
        self.bd.session.commit()