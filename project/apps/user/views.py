from flask import Blueprint, current_app, url_for, request, session, g
from werkzeug.security import check_password_hash
from project.utils.template import render, redirect
from project.utils.auth import admin
from .forms import LoginForm
from .models import User


mod = Blueprint('user', __name__, url_prefix='/admin')


@mod.route('/', methods=['POST', 'GET'])
def login():
    if g.user.can('login'):
        return redirect(url_for('user.dashboard'))
    form = LoginForm(request.form)
    if request.method != 'POST':
        return render('admin/login.html', form=form)
    form.validate()
    if form.errors != dict():
        return render('admin/login.html', form=form)
    email = form.email.data
    password = form.password.data
    try:
        user = User.objects.get(email=email)
        print check_password_hash(password, user.password)
    except:
        msg = 'user password not matched'
        return render('admin/login.html', form=form, msg=msg)
    session['email'] = user.email
    return redirect(url_for('user.dashboard'))


@mod.route('/dashboard/')
@admin
def dashboard():
    return render('index.html')
