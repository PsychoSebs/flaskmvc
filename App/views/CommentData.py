from flask import Blueprint, redirect, render_template, request, send_from_directory, flash, url_for
from App.views.api import LoginManager, UserMixin,login_required,current_user
from App.models.forms import UserData
from App.models.CommentHistory import UserRecords, UserComment
from App.models.user import User
from App.controllers.CommentFunc import create_record, createComment
from App.database import db
from sqlalchemy.exc import IntegrityError
import json

CommentData_views = Blueprint('CommentData_views', __name__, template_folder='../templates')

@CommentData_views.route('/dataForm', methods=['GET'])
def getData():
    myForm = UserData()
    return render_template('GetuserData.html',myForm=myForm)

@CommentData_views.route('/getData', methods=['POST'])
@login_required
def PostData():
    myForm = UserData()
    if myForm.validate_on_submit():
        formData=request.form

        try:
            createComment(formData["topic"], formData["comment"])
        except IntegrityError:
            db.session.rollback()
            print(formData["topic"], formData["comment"])
        
        flash('Your information has been recorded!')
        #return redirect("/mainPage")
        return redirect(url_for('mainPage_views.show_main'))
    flash('Error invalid input!')
    return render_template('GetuserData.html',myForm=myForm)


@CommentData_views.route("/showData", methods=['GET'])
@login_required
def showInfo():
    data = {}
    topics = db.session.query(UserComment.topic).distinct()
    for topic in topics:
        comments = UserComment.query.filter_by(topic=topic.topic).all()
        data[topic.topic] = comments
         

    return render_template("ShowUserData.html",data=data)

        
