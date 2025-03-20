from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class IngresoForm(FlaskForm):
    correo = EmailField('Correo', validators=[InputRequired(
        message="El correo es requerido."
    ), Email(
        message="El correo no es válido."
    )])
    
    password = PasswordField('Contraseña', validators=[InputRequired(
        message="La contraseña es requerida."
    ), Length(
        min=4, 
        max=50,
        message="La contraseña debe tener entre 4 y 50 caracteres."
    )])
    
    recordarme = BooleanField('Recordarme')