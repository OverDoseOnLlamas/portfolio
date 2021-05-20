from types import new_class
from flask import Flask, render_template, request, redirect
from flask.templating import render_template_string
app = Flask(__name__)
import csv
#BOOTSTRAP GOOGLE

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/index.html')
def index():
    return render_template('./index.html')    

@app.route('/works.html')
def works():
    return render_template('./works.html')

@app.route('/about.html')
def about():
    return render_template('./about.html')

@app.route('/contact.html')
def contact():
    return render_template('./contact.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "work in progress"

# @app.route('/works.html')
# def works():
#     return render_template('./works.html')

# @app.route('/about.html')
# def about():
#     return render_template('./about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('./components.html')


