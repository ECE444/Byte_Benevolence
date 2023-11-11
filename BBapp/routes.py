from flask import Flask, render_template, session, redirect, url_for, flash, Blueprint, request, jsonify
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

    if request.method == 'POST':
        errors = []
        signupUser = {}  # For now, just store in a dictionary; change this to User object later

        if "utoronto" not in form.email.data:
            errors.append("Please use a valid UofT email address")

        if form.password.data != form.confirmPassword.data:
            errors.append("Passwords do not match")

        if form.clubRepresentative.data == 'Yes':
            if not roleForm.clubName.data.strip():
                errors.append("Please enter a club name")

        if (len(errors) > 0):
            return render_template('signup.html', form=form, roleForm=roleForm, errors=errors)

        signupUser['email'] = form.email.data
        signupUser['name'] = form.name.data
        signupUser['phone'] = form.phone.data
        signupUser['password'] = form.password.data

        if form.clubRepresentative.data == 'No':
            signupUser['clubRepresentative'] = False
            signupUser['clubName'] = ""
            signupUser['clubRole'] = ""
        else:
            signupUser['clubRepresentative'] = True
            signupUser['clubName'] = roleForm.clubName.data
            signupUser['clubRole'] = roleForm.clubRole.data

        # call method to save user data to the database here
        session['email'] = signupUser['email']
        session['logged_in'] = True
        return redirect(url_for('user_page.user'))

    return render_template('signup.html', form=form, roleForm=roleForm, errors=[])


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

calendar_page = Blueprint('calendar_page', __name__, template_folder='templates')
@calendar_page.route('/calendar', methods=['GET', 'POST'])
def calendar():
    return render_template('calendar.html', logged_in=session.get('logged_in'), email=session.get('email'), current_time=datetime.utcnow())

@calendar_page.route("/receiver", methods=['GET', 'POST'])
def postME():
   data = {"name": "test1", "value": 0}
   data = jsonify(data)
   return data