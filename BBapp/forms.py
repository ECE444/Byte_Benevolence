#this file is for the forms
#app is the Flask object created in __init__.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,RadioField
from wtforms.validators import DataRequired, Email


class SignupForm(FlaskForm):
    email = StringField('UofT Email Address', validators=[Email()])
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    confirmPassword = StringField('Confirm Password', validators=[DataRequired()])
    clubRepresentative = SelectField('Are you a club representative?', choices=[('Yes', 'Yes'), ('No', 'No')],id='clubRepresentative', validators=[DataRequired()])
    submit = SubmitField('Signup')

class RoleForm(FlaskForm):
    roleOptions = ['President', 'Vice President', 'Treasurer', 'Secretary', 'Events Coordinator', 'Social Media Coordinator']
    clubName = StringField('Club Name', validators=[DataRequired()])
    clubRole = SelectField('Role', choices=[(role, role) for role in roleOptions], validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = StringField('UofT Email Address', validators=[Email()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class LogoutForm(FlaskForm):
    submit = SubmitField('Logout')

