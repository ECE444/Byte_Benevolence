from flask import Flask, render_template, session, redirect, url_for, flash, Blueprint
from datetime import datetime
from  BBapp.forms import *

home_page = Blueprint('home_page', __name__, template_folder='templates')
@home_page.route('/')
def home():
    return render_template('index.html', current_time=datetime.utcnow())


signup_page = Blueprint('signup_page', __name__, template_folder='templates')
@signup_page.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    roleForm = RoleForm()
    return render_template('signup.html', form = form , roleForm = roleForm)

login_page = Blueprint('login_page', __name__, template_folder='templates')
@login_page.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in') != True:
        form = LoginForm()
        if form.validate_on_submit():
            session['email'] = form.email.data
            if 'utoronto' in session.get('email'):
                session['valid_email'] = True
            else:
                session['valid_email'] = False
                return redirect(url_for('login_page.login'))
            
            session['password'] = form.password.data
            if session.get('password') == 'password':
                session['logged_in'] = True
                return redirect(url_for('user_page.user'))
            return redirect(url_for('login_page.login'))
        return render_template('login.html', logged_in=session.get('logged_in'), form=form, email=session.get('email'), validEmail=session.get('valid_email'), current_time=datetime.utcnow())
    else:
        form = LogoutForm()
        if form.validate_on_submit():
            session['logged_in'] = False
            session['email'] = None
            session['password'] = None
            session['valid_email'] = None
            return redirect(url_for('login_page.login'))
        return render_template('login.html', logged_in=session.get('logged_in'), form=form, email=session.get('email'), current_time=datetime.utcnow())

user_page = Blueprint('user_page', __name__, template_folder='templates')
@user_page.route('/user')
def user():
    return render_template('user.html', logged_in=session.get('logged_in'), email=session.get('email'), current_time=datetime.utcnow())