from flask import Flask, render_template, request
from flask_wtf import FlaskForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'youwillneverguess'

@app.route('/', methods=["GET","POST"])
def index():
    return "Hiya"