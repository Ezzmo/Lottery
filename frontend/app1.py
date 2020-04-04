from flask import Flask, request, render_template, redirect, url_for, request, session
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import SubmitField, StringField, validators
import requests
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://madmin:adminpass@localhost:3307/db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class EntryForm(FlaskForm):
    firstname = StringField('First name',[validators.DataRequired()])
    lastname = StringField('Last name', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(),validators.Email()])
    submit = SubmitField('Enter')
#    def validate_email(self,email):
#        user = Entries.query.filter_by(email=email.data).first()
#        if user:
#            raise ValidationError('Email already entered!')

class entries(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    code = db.Column(db.String(6), nullable=False)

@app.route('/')
@app.route('/home', methods=['GET','POST', 'PUT'])
def home():
    form = EntryForm()
    if request.method=='POST' and form.validate():
        name = form.firstname.data + " " + form.lastname.data
        code = str(requests.get('http://backend:5001/roll').text)
        email = form.email.data
        entrant = entries(
#            firstname=form.firstname.data,
#            lastname=form.lastname.data,
#            email=form.email.data,
#            code=str(requests.get('http://backend:5001/roll').text)
#        )
#        session['entrant']=entrant
#        db.session.add(entrant)
#        db.session.commit()
        return redirect(url_for('home', name=name, code=code, email=email))
    return render_template('indexq.html')

#@app.route('/entered', methods=['GET','POST','PUT'])
#def entered():
#    name = ""
#    code = ""
#    return render_template('landing.html',name=name, code=code)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')