from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = ']%<96hX:3Pv+'
bootstrap = Bootstrap(app)
moment = Moment(app)

from BBapp.routes import *
app.register_blueprint(login_page)
