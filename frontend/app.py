from flask import Flask, request, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import SubmitField
import wtforms.validators
import requests
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

class rollbutton(FlaskForm):
    roll = SubmitField()

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    form = rollbutton()
    roll = str(requests.get('http://backend:5001/roll').text)
    return render_emplate('index.html',form=form, roll=roll)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')