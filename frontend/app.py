from flask import Flask, request, render_template, redirect, url_for, request, session
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import SubmitField, StringField, validators
import requests
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://madmin:adminpass@databass:3306/lottery"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class entries(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(6), nullable=False)

@app.route('/')
@app.route('/home')
def home():
   return render_template('index.html')

@app.route('/entry',methods = ['POST', 'GET'])
def entry():
    if request.method == 'POST':
        entry = request.form
        code = str(requests.get('http://backend:5001/roll').text)
        entryval={}
        for key, value in entry.items():
            entryval.update({key : value})
        entryval.update({'Code' : code})    
        dbentry = entries(first_name=entryval['First Name'], last_name=entryval['Last Name'], code= code)
        db.session.add(dbentry)
        db.session.commit()
        return render_template("entry.html",entry = entry, code=code)
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')