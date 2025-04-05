from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired

class RecipeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    url = StringField('URL')
    description = TextAreaField('Description')
    pdf = FileField('PDF File')
    submit = SubmitField('Submit')