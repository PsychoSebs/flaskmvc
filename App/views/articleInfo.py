from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from flask_login import LoginManager, UserMixin,login_required,current_user
from App.models.CommentHistory import UserRecords
from App.controllers.CommentFunc import getComments


article_views = Blueprint('article_views', __name__, template_folder='../templates')

@article_views.route('/1-alcohol', methods=['GET'])
@login_required
def show1():
    #myForm = UserData()
    data = {}
    comments = getComments("Alcohol")
    for comment in comments:
        data[comment.comment] = comment.record[0].user.username
    return render_template('1-alcohol.html',data = data)

@article_views.route('/2-artificial_intelligence', methods=['GET'])
@login_required
def show2():
    #myForm = UserData()
    data = {}
    comments = getComments("AI")
    for comment in comments:
        data[comment.comment] = comment.record[0].user.username
    return render_template('2-artificial_intelligence.html', data = data)

@article_views.route('/3-bees', methods=['GET'])
@login_required
def show3():
    #myForm = UserData()
    data = {}
    comments = getComments("Bees")
    for comment in comments:
        data[comment.comment] = comment.record[0].user.username
    return render_template('3-bees.html', data = data)

@article_views.route('/4-cyberbullying', methods=['GET'])
@login_required
def show4():
    #myForm = UserData()
    data = {}
    comments = getComments("Cyber Bullying")
    for comment in comments:
        data[comment.comment] = comment.record[0].user.username
    return render_template('4-cyberbullying.html',data = data)

@article_views.route('/5-sleep', methods=['GET'])
@login_required
def show5():
    #myForm = UserData()
    data = {}
    comments = getComments("Sleep")
    for comment in comments:
        data[comment.comment] = comment.record[0].user.username
    return render_template('5-sleep.html', data = data)

@article_views.route('/6-stress', methods=['GET'])
@login_required
def show6():
    #myForm = UserData()
    data = {}
    comments = getComments("Stress")
    for comment in comments:
        data[comment.comment] = comment.record[0].user.username
    return render_template('6-stress.html',data = data)