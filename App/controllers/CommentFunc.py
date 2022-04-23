from App.models import UserRecords, User, UserComment
from flask_login import LoginManager, UserMixin,login_required,current_user
from App.models.user import User
from App.database import db
import uuid

def createComment(topic,comment):
    newComment = UserComment(commentID=str(uuid.uuid4()), topic=topic,comment=comment)
    db.session.add(newComment)
    db.session.commit()
    create_record(newComment.commentID, current_user.id)

def create_record(commentID,user_id):
    newrecord= UserRecords(postNum=str(uuid.uuid4()),commentID=commentID,user_id=user_id)
    db.session.add(newrecord)
    db.session.commit()

def get_all_users_json():
    records = UserRecords.query.all()
    if not records:
        return []
    records = [record.toDict() for record in records]
    return users

def get_all_users():
    return UserRecords.query.all()

def getComments(topic):
    comments = UserComment.query.filter_by(topic=topic).all()
    return comments

