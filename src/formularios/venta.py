from flask_wtf import FlaskForm
from wtforms import EmailField
from wtforms.validators import Optional, Length

class VentaForm(FlaskForm):
    email_comprador = EmailField('Correo del Comprador', validators=[Length(min=5, max=50), Optional()])