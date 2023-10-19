#this file is for the forms
#app is the Flask object created in __init__.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('UofT Email Address', validators=[Email()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class LogoutForm(FlaskForm):
    submit = SubmitField('Logout')