from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired

class RecipeForm(FlaskForm):
    name = StringField('Jméno', validators=[DataRequired()])
    url = StringField('URL')
    description = TextAreaField('Popis')
    pdf = FileField('PDF Soubor')
    submit = SubmitField('Odeslat')