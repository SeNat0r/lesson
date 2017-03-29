from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, FloatField, SelectField
from wtforms.validators import DataRequired, Optional


class CategoryForm(FlaskForm):
    id = HiddenField()
    title = StringField('Наименования', validators=[DataRequired()])
