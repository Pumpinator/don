from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import HiddenField, StringField, FloatField, FileField
from wtforms.validators import DataRequired, Length, InputRequired, NumberRange

class AgregarGalleta(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message="El nombre del insumo es obligatorio."),
        Length(min=1, max=50, message="El nombre debe tener entre 1 y 50 caracteres.")
    ])
    precio = FloatField('Precio', validators=[
        DataRequired(message="El precio es obligatorio."),
        NumberRange(min=0, message="El precio debe ser un número positivo.")
    ])
    imagen = FileField('Imagen', validators=[
        DataRequired(message="La imagen es obligatoria."),
        FileAllowed(['jpg', 'jpeg', 'png'], message="Solo se permiten imágenes en formato JPG o PNG.")
    ])
    
class EditarGalleta(FlaskForm):
    id = HiddenField('Id')
    nombre = StringField('Nombre', validators=[
        InputRequired(message="El nombre es requerido"),
        Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres")
    ])
    precio = FloatField('Precio', validators=[
        InputRequired(message="El precio es requerido"),
        NumberRange(min=0, message="El precio debe ser un número positivo.")
    ])