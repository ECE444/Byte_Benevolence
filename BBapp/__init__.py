from flask import Flask, render_template, session, redirect, url_for, flash
from flask_cors import CORS
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = ']%<96hX:3Pv+'
bootstrap = Bootstrap(app)
moment = Moment(app)

from BBapp.routes import *
app.register_blueprint(home_page)
app.register_blueprint(login_page)
app.register_blueprint(user_page)
app.register_blueprint(signup_page)
app.register_blueprint(calendar_page)