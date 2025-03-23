from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, NumberRange

class MermaForm(FlaskForm):
    tipo_merma = SelectField('Tipo de Merma', choices=[
        ('insumo', 'Insumo'),
        ('galleta', 'Galleta'),
        ('produccion', 'Producción')
    ], validators=[DataRequired()])
    
    item_id = IntegerField('ID del Item', validators=[DataRequired(), NumberRange(min=1, message="Debe ser un número válido")])
    medida = IntegerField('ID de la Medida', validators=[DataRequired()])
    cantidad = FloatField('Cantidad', validators=[DataRequired()])
