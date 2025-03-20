from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[InputRequired(
        message="El nombre es requerido"
    ), Length(
        min=2,
        max=50,
        message="El nombre debe tener entre 2 y 50 caracteres"
    )])
    
    email = EmailField('Correo', validators=[InputRequired(
        message="El correo es requerido"
    ), Email(
        message="El correo no es válido"
    ), Length(
        min=4, 
        max=50,
        message="El correo debe tener entre 4 y 50 caracteres"
    )])
    
    password = PasswordField('Contraseña', validators=[InputRequired(
        message="La contraseña es requerida"
    ), Length(
        min=4,
        max=50,
        message="La contraseña debe tener entre 4 y 50 caracteres"
    )])
    
    confirm_password = PasswordField('Confirmar contraseña', validators=[InputRequired(
        message="La confirmación de la contraseña es requerida"
    ), EqualTo(
        'password',
        message='Las contraseñas deben coincidir'
    )])