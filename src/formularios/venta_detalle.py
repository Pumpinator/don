from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired
from modelo.galleta import Galleta

class VentaDetalleForm(FlaskForm):
    galleta_id = SelectField('Galleta', coerce=int, validators=[DataRequired()])
    cantidad = FloatField('Cantidad', validators=[DataRequired()])
    medida_id = IntegerField('Medida ID', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(VentaDetalleForm, self).__init__(*args, **kwargs)
        self.galleta_id.choices = [(g.id, g.nombre) for g in Galleta.query.all()]