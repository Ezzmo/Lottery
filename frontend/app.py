from flask import Flask, request, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import SubmitField, StringField
import wtforms.validators
import requests
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://madmin:adminpass@http://db:3306/db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Entries(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    code = db.Column(db.String(6), nullable=False)

class EntryForm(FlaskForm):
	firstname = StringField('First name',
		validators=[
			DataRequired(),
		])
	lastname = StringField('Last name',
		validators=[
			DataRequired(),
		])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
	submit = SubmitField('Enter')

    def validate_name(self, email):
        user = Players.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Name already in database')

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    form = EntryForm()
     if form.validate_on_submit():
        entrant = [
            form.firstname.data,
            form.lastname.data,
            form.email.data,
            str(requests.get('http://backend:5001/roll').text)
        ]
        entrantfordb = entries(first_name=entrant[0], last_name=entrant[1], email = entrant[2], code = entrant[3])
        db.session.add(entrantfordb)
        db.session.commit()
        return redirect(url_for('entered'), entrant=entrant)
    return render_emplate('index.html',form=form, roll=roll)

@app.route('/entered')
def entered():
    entrant=[]
    return render_template('landing.html',entrant=entrant)
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')