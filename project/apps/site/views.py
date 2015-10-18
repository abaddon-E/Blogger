from flask import Blueprint, current_app, url_for, g
from project.utils.template import render, redirect
from project.apps.user.forms import LoginForm, RegistrationForm


mod = Blueprint('site', __name__)


@mod.route('/')
def landing():
    login_form = LoginForm()
    register_form = RegistrationForm()
    print '#' * 50
    print g.base_site.current
    print g.base_site.is_front
    print '#' * 50
    return render('landings/blogger/landing.html',
                  login_form=login_form,
                  register_form=register_form)

@mod.route('/asghar')
def asghar():
    return redirect(url_for('site.landing'))
