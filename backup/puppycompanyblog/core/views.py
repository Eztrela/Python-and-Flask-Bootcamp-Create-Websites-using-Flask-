#core/views.py

from flask import Blueprint, render_template, request

core = Blueprint('core',__name__)

@core.route('/')
def index():
    # MORE TO COME
    return render_template('index.html')

@core.route('/info')
def info ():
    return render_template('info.html')