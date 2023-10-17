from flask import Flask, render_template, session, redirect, url_for, flash, Blueprint
from datetime import datetime
#app is the Flask object created in __init__.py
from BBapp import app 
from BBapp.forms import LoginForm

login_page = Blueprint('login_page', __name__, template_folder='templates')

@login_page.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        old_email = session.get('email')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['email'] = form.email.data
        if 'utoronto' in session['email']:
            session['validEmail'] = True
        else:
            session['validEmail'] = False
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'), validEmail=session.get('validEmail'), current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())