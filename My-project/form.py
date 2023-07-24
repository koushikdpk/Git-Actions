from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired


class EmployeeForm(FlaskForm):
    name = StringField('Employee Name', validators=[InputRequired()])
    designation = StringField('Designation', validators=[InputRequired()])
    role = StringField('Role', validators=[InputRequired()])
    experience = IntegerField('Experience', validators=[InputRequired()])
    submit = SubmitField(label='Submit')
