from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class BlockForm(FlaskForm):

    contract = StringField('Floor', validators=[DataRequired()])
    save = SubmitField('Save')
