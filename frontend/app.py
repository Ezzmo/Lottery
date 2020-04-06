from flask import Flask, request, render_template, redirect, url_for, request, session
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import SubmitField, StringField, validators
import requests
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:"+getenv('DB_ROOT_PASS')+"@databass:3306/lottery"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class entries(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(8), nullable=False)
    email = db.Column(db.String(50),nullable=False)
    winnings = db.Column(db.String(6), nullable=False)

@app.route('/')
@app.route('/home')
def home():
   return render_template('index.html')

@app.route('/entry',methods = ['POST', 'GET'])
def entry():
    vowels="aeiou"
    if request.method == 'POST':
        entry = request.form.to_dict()
        code = str(requests.get('http://backend:5001/roll').text)
        entry.update({'Code' : code})
        if code[1] in vowels and code[2] in vowels and code[-1]==9:
            entry.update({'Winnings' : "£1000"})
        elif (code[1] in vowels or code[2] in vowels) and code[-1] ==9:
            entry.update({'Winnings' : '£100'})
        elif code[-1] == 9 or code[1] in vowels:
            entry.update({'Winnings' : '£10'})
        else:
            entry.update({'Winnings' : '£0'})
        dbentry = entries(first_name=entry['First Name'], last_name=entry['Last Name'], email=entry['Email'], code= code, winnings=entry['Winnings'])
        db.session.add(dbentry)
        db.session.commit()
        return render_template("entry.html",entry = entry, code=code)
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')