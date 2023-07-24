from app import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique= True)

    def __init__(self,username,password,name,email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<user %r>" % self.username


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    user = db.relationship('User',foreign_keys=user_id)
    
    def __init__(self,content,user_id):
        self.content = content
        self.user_id = user_id


    def __repr__(self):
        return "<posts %r>" % self.id
    


class Follow(db.Model):
    __tablename__ = "follows"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)