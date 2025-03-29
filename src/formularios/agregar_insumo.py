from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField
from wtforms.validators import DataRequired, Length, InputRequired

class AgregarInsumo(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message="El nombre del insumo es obligatorio."),
        Length(min=1, max=50, message="El nombre debe tener entre 1 y 50 caracteres.")
    ])
class EditarForm(FlaskForm):
    id = HiddenField('Id')
    nombre = StringField('Nombre', validators=[
        InputRequired(message="El nombre es requerido"),
        Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres")
    ])