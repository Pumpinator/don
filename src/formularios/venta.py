from flask_wtf import FlaskForm
from wtforms import EmailField, DateTimeLocalField, HiddenField
from wtforms.validators import Optional, Length
from datetime import datetime, time

class VentaForm(FlaskForm):
    venta_id = HiddenField('ID de Venta', validators=[Optional()])
    
    email_comprador = EmailField('Correo del Comprador', validators=[Length(min=5, max=50), Optional()])

    fecha_entrega = DateTimeLocalField(
        'Fecha de Entrega',
        validators=[Optional()],
        render_kw={
            "min": datetime.now().strftime('%Y-%m-%dT%H:%M'),
            "max": datetime.combine(datetime.now().date(), time(20, 0)).strftime('%Y-%m-%dT%H:%M')
        }
    )