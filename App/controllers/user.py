from App.models import User
from App.database import db
import uuid
from sqlalchemy.exc import IntegrityError

def get_all_users():
    return User.query.all()


def create_user(username,email, password):
    newuser =User(id=str(uuid.uuid4()),username=username,email=email,password=password)
    try:
        db.session.add(newuser)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        flash("username already exist")
        

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def get_all_users():
    return User.query.all()