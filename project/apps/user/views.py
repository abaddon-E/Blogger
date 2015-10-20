from flask import Blueprint, current_app, url_for, request, session, g
from werkzeug.security import check_password_hash, generate_password_hash
from project.utils.template import render, redirect
from project.utils.auth import admin
from .forms import LoginForm
from .models import User


mod = Blueprint('user', __name__, url_prefix='/admin')


def email_normalizer(email):
    email = email.lower().strip()
    if '@gmail.com' in email:
        email = eamil.split('@gmail.com')[0].replace('.', '') + \
                eamil.split('@gmail.com')[1]
    return email


@mod.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method != 'POST':
        return render('login.html', login_form=form)
    form.validate()
    if form.errors != dict():
        return render('login.html', login_form=form)
    email = email_normalizer(form.email.data)
    password = form.password.data
    try:
        user = User.objects.get(email=email)
        if not check_password_hash(password, user.password):
            raise
    except:
        msg = 'user password not matched'
        return render('login.html', login_form=form, msg=msg)
    session['email'] = user.email
    return redirect(url_for('user.dashboard'))


@mod.route('/register')
def register():
    form = RegistrationForm(request.form)
    if request.method != 'POST':
        return render('register.html', register_form=form)
    form.validate()
    if form.errors != dict():
        return render('register.html', register_form=form)
    email = email_normalizer(form.email.data)
    password = generate_password_hash(form.password.data)
    if User.objects(email=email).first():
        msg = 'email exists'
        return render('register.html', register_form=form, msg=msg)
    user = User(email=email, password=password, name=form.name.data).save()
    session['email'] = user.email
    return redirect(url_for('user.dashboard'))


@mod.route('/dashboard/')
@admin
def dashboard():
    return render('index.html')
