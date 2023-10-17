#this file is for the forms
#app is the Flask object created in __init__.py
from BBapp import app 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('What is your UofT Email address?', validators=[Email()])
    password = StringField('What is your password?', validators=[DataRequired()])
    submit = SubmitField('Submit')