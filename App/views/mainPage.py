from flask import Blueprint, render_template, jsonify, request, send_from_directory, url_for
from flask_jwt import jwt_required
from flask_login import LoginManager, UserMixin,login_required,current_user
import json
import requests

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)

mainPage_views = Blueprint('mainPage_views', __name__, template_folder='../templates')

@mainPage_views.route('/mainPage', methods = ['GET'])
@login_required
def show_main():

    return render_template('index.html')
