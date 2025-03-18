from wtforms import Form
from flask_wtf import FlaskForm
 
from wtforms import StringField,IntegerField
from wtforms import EmailField
from wtforms import validators

class UseForm(Form):
    nombre=StringField('Nombre/s',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='ingresa nombre valido')
    ])
    apellido=StringField('Apellido')
    email=EmailField('Email',[ validators.Email(message='Ingrese un correo valido')])
    contrasenia=StringField('Contraseña',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=8,max=100, message='ingresa una contraseña valida')
    ])