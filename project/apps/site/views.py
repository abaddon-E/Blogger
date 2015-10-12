from flask import Blueprint, current_app, url_for
from project.utils.template import render, redirect

mod = Blueprint('site', __name__)

@mod.route('/')
def landing():
    return render('index.html')

@mod.route('/asghar')
def asghar():
    return redirect(url_for('site.landing'))
