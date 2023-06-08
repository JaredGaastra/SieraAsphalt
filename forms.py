from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import DataRequired

class QuoteForm(FlaskForm):
    project_name = StringField('name', validators=[DataRequired()])
    project_description = StringField('description', validators=[DataRequired()])
    budget = IntegerField('budget', validators=[DataRequired()])
    start_date = DateField('start_date', validators=[DataRequired()])




