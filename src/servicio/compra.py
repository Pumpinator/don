from sqlalchemy import text
from sqlalchemy.orm import joinedload
from modelo.compra import Compra
from modelo.compra_detalle import CompraDetalle
from modelo.insumo_inventario import InsumoInventario
from modelo.proveedor import Proveedor
from modelo.insumo import Insumo
from modelo.medida import Medida

class CompraServicio:
    
    def __init__(self, bd):
        self.bd = bd
        
    def obtener_compras(self):
        resultados = (
            self.bd.session.query(
                Compra.id,
                Compra.fecha,
                Compra.total,
                Proveedor.nombre.label('proveedor_nombre'),
                Insumo.nombre.label('insumo_nombre'),
                CompraDetalle.cantidad,
                CompraDetalle.precio_unitario,
                Medida.nombre.label('medida_nombre'),
                Medida.abreviatura.label('medida_abreviatura')
            )
            .join(Compra.proveedor)
            .join(CompraDetalle, Compra.detalles)
            .join(Insumo, CompraDetalle.insumo)
            .join(Medida, CompraDetalle.medida)
            .order_by(Compra.fecha.desc())
            .all()
        )

        compras_dict = {}
        for row in resultados:
            compra_id = row.id
            
            if compra_id not in compras_dict:
                compras_dict[compra_id] = {
                    'id': compra_id,
                    'fecha': row.fecha.strftime('%d/%m/%Y'),
                    'total':  f"{float(row.total):,.2f}",
                    'proveedor': row.proveedor_nombre,
                    'insumos': []
                }
                
            compras_dict[compra_id]['insumos'].append({
                'nombre': row.insumo_nombre,
                'cantidad': f"{row.cantidad} {row.medida_abreviatura}",
            })

        return list(compras_dict.values())
    
    def obtener_proveedores(self):
        return self.bd.session.query(Proveedor).all()
    
    def obtener_insumos(self):
        return self.bd.session.query(Insumo).all()
    
    def obtener_medidas(self):
        return self.bd.session.query(Medida).all()
    
    def obtener_proveedor(self, proveedor_id):
        return self.bd.session.query(Proveedor).get(proveedor_id)
    
    def crear_compra(self, compra_data):
        try:
            query = text("""
                CALL SP_CrearCompra(
                    :proveedor_id, 
                    :fecha, 
                    :total, 
                    :insumos, 
                    :cantidades, 
                    :precios_unitarios, 
                    :medidas, 
                    :fechas_expiracion
                )
            """)
            
            params = {
                'proveedor_id': compra_data['proveedor_id'],
                'fecha': compra_data['fecha'],
                'total': compra_data['total'],
                'insumos': ','.join(compra_data['insumos']),
                'cantidades': ','.join(compra_data['cantidades']),
                'precios_unitarios': ','.join(compra_data['precios_unitarios']),
                'medidas': ','.join(compra_data['medidas']),
                'fechas_expiracion': ','.join(compra_data['fechas_expiracion'])
            }
            
            self.bd.session.execute(query, params)
            self.bd.session.commit()
            return True
        except Exception as e:
            self.bd.session.rollback()
            raise e

    def obtener_compra(self, compra_id):
        query = (
            self.bd.session
            .query(
                Insumo.nombre,
                CompraDetalle.cantidad,
                CompraDetalle.precio_unitario,
                CompraDetalle.insumo_id,
                CompraDetalle.precio_total,
                Medida.nombre,
                Medida.abreviatura
            )
            .select_from(Compra)
            .join(CompraDetalle, Compra.id == CompraDetalle.compra_id)
            .join(Insumo, CompraDetalle.insumo_id == Insumo.id)
            .join(Medida, CompraDetalle.medida_id == Medida.id)
            .filter(Compra.id == compra_id)
        )
        
        resultados = query.all()
        
        detalles = [
            {
                "insumo": insumo,
                "cantidad": cantidad,
                "precio_unitario": precio_unitario,
                "insumo_id": insumo_id,
                "precio_total": precio_total,
                "medida_nombre": medida,
                "medida_abreviatura": medida_abreviatura
            }
            for insumo, cantidad, precio_unitario, insumo_id, precio_total, medida, medida_abreviatura in resultados
        ]
        
        query = (
            self.bd.session
            .query(Compra.fecha, Proveedor.nombre)
            .join(Proveedor, Compra.proveedor_id == Proveedor.id)
            .filter(Compra.id == compra_id)
        )
        fecha, proveedor = query.first()
        compra = {
            "id": compra_id,
            "fecha": fecha.strftime('%d/%m/%Y'),
            "proveedor": proveedor,
            "detalles": detalles,
            "total": f"{float(sum(d['precio_total'] for d in detalles)):,.2f}"
        }
        return compra

    def editar_compra(self, compra_id, compra_data):
        try:            
            compra = self.bd.session.query(Compra).get(compra_id)
            compra.proveedor_id = compra_data['proveedor_id']
            compra.fecha = compra_data['fecha']
            
            existing_details = {d.insumo_id: d for d in compra.detalles}
            nuevo_total = 0
            
            for i in range(len(compra_data['insumos'])):
                insumo_id = int(compra_data['insumos'][i])
                cantidad = float(compra_data['cantidades'][i])
                precio = float(compra_data['precios_unitarios'][i])
                medida_id = int(compra_data['medidas'][i])
                
                subtotal = cantidad * precio
                nuevo_total += subtotal
                
                if insumo_id in existing_details:
                    detalle = existing_details[insumo_id]
                    detalle.cantidad = cantidad
                    detalle.precio_unitario = precio
                    detalle.medida_id = medida_id
                else:
                    detalle = CompraDetalle(
                        compra_id=compra_id,
                        insumo_id=insumo_id,
                        cantidad=cantidad,
                        precio_unitario=precio,
                        medida_id=medida_id
                    )
                    self.bd.session.add(detalle)
                
                inventario = self.bd.session.query(InsumoInventario).filter_by(
                    compra_id=compra_id,
                    insumo_id=insumo_id
                ).first()
                
                if inventario:
                    inventario.fecha_expiracion = compra_data['fechas_expiracion'][i] or None
                    inventario.costo = precio
                    inventario.cantidad = cantidad
                    inventario.medida_id = medida_id
                else:
                    nuevo_inventario = InsumoInventario(
                        compra_id=compra_id,
                        insumo_id=insumo_id,
                        fecha_expiracion=compra_data['fechas_expiracion'][i] or None,
                        costo=precio,
                        cantidad=cantidad,
                        medida_id=medida_id
                    )
                    self.bd.session.add(nuevo_inventario)
            
            compra.total = nuevo_total
            
            submitted_insumo_ids = {int(id) for id in compra_data['insumos']}
            for detalle in compra.detalles:
                if detalle.insumo_id not in submitted_insumo_ids:
                    self.bd.session.delete(detalle)
                    self.bd.session.query(InsumoInventario).filter_by(
                        compra_id=compra_id,
                        insumo_id=detalle.insumo_id
                    ).delete()
            
            self.bd.session.commit()
            return True
            
        except Exception as e:
            self.bd.session.rollback()
            raise e