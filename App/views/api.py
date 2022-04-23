from flask import Blueprint, redirect, render_template, request, send_from_directory, flash, url_for
from flask_login import LoginManager, UserMixin, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from App.models.forms import SignUp, LogIn
from App.models.user import User
from App.controllers import *
from App.controllers.auth import login_user, authenticate, identity, setup_jwt

api_views = Blueprint('api_views', __name__, template_folder='../templates')

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)

@api_views.route('/', methods=['GET'])
def signup():
    myForm = SignUp()
    return render_template('signup.html',myForm=myForm)

@api_views.route('/signup', methods=['POST'])
def signupUser():
  form=SignUp()
  if form.validate_on_submit():
    formData=request.form
    create_user(formData["username"],formData["email"],formData["password"])
    flash('Your Account Has Been Created!')
    redirect(url_for('api_views.getLogin'))
    return redirect(url_for('api_views.getLogin'))
  flash('Error invalid input!')
  return redirect(url_for('api_views.signup'))


@api_views.route('/login', methods=['GET'])
def getLogin():
  myForm=LogIn()
  return render_template('login.html', myForm=myForm)


@api_views.route('/loginUser', methods=['POST'])
def loginAction():
  form = LogIn()
  if form.validate_on_submit():
      data = request.form
      user = authenticate(data["username"],data["password"])
      if user and user.check_password(data['password']):
        login_user(user,remember=True)
        flash('You have Logged in successfully.')
        return redirect(url_for('mainPage_views.show_main'))
      flash('Invalid credentials')
      myForm=LogIn()
      return render_template('login.html',myForm=myForm)

@api_views.route('/logout', methods=['GET'])
@login_required
def logout():
  logout_user()
  flash('Logged Out!')
  return redirect(url_for('api_views.getLogin')) 