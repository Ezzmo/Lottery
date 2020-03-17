from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from application.forms import ChooseForm, RegistrationForm, LoginForm, UpdateTeamForm
from application.models import Userteams, Users, Players
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    render_template('index.html')