from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, FloatField, SelectField, DateField
from wtforms.validators import InputRequired, Length

class AgregarInsumo(FlaskForm):
    nombre = StringField('Nombre del insumo', validators=[InputRequired(
        message="El nombre es requerido.")
    ])

    unidad_medida = SelectField('Unidad de Medida', choices=[
        ('1', 'Kilogramos'),
        ('2', 'Litros'),
        ('3', 'Unidades')
    ], validators=[InputRequired(
        message="La unidad de medida es requerida."
    )])
    
    costo = StringField('Costo', validators=[InputRequired(
        message="La costo es requerida."
    )])
    
    fecha_expiracion = DateField('Fecha de expiración', validators=[
        InputRequired(message="La fecha de expiración es requerida."),
        Length(min=10, max=10, message="La fecha de expiración debe tener 10 caracteres.")
        ])
    
    cantidad = FloatField('Cantidad', validators=[InputRequired(
        message="La cantidad es requerida."
    )])
