from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, DateField, FieldList, FormField
from wtforms.validators import DataRequired
from formularios.venta_detalle import VentaDetalleForm

class VentaForm(FlaskForm):
    comprador_id = IntegerField('Comprador ID', validators=[DataRequired()])
    vendedor_id = IntegerField('Vendedor ID', validators=[DataRequired()])
    pagado = BooleanField('Pagado')
    fecha_entrega = DateField('Fecha de Entrega', format='%Y-%m-%d', validators=[DataRequired()])
    detalles = FieldList(FormField(VentaDetalleForm), min_entries=1)