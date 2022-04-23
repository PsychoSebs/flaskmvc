from App.database import db
from App.models.user import User

class UserComment(db.Model):
    commentID = db.Column(db.String(120), primary_key=True)
    topic = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(50), nullable=False)
    record=db.relationship('UserRecords', backref='comments', cascade='all, delete-orphan' , lazy='dynamic')

class UserRecords(db.Model):
    postNum = db.Column(db.String(120), primary_key=True)
    commentID = db.Column(db.String(120), db.ForeignKey(UserComment.commentID))
    user_id= db.Column(db.String(120), db.ForeignKey(User.id))

    def __init__(self,postNum,commentID,user_id):
        self.postNum=postNum
        self.commentID=commentID
        self.user_id=user_id

    def toDict(self):
        return{
            'postNum':self.postNum,
            'commentID':self.commentID,
            'user_id':self.user_id
        }



    