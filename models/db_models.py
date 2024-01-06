"""
    File for the databases sqlalchemy models
"""

from models import db, login_manager
from datetime import datetime
from flask_login import UserMixin

# Fucntion decorator for flask login to manager logins and sessions.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    tweets = db.relationship('Tweet', back_populates='author')

    def __repr__(self):
        return f"User ({self.username} - {self.email})"

class Tweet(db.Model):
    __tablename__ = "tweets"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    author = db.relationship('User', back_populates='tweets')

    def __repr__(self):
        return f"Tweet ({self.author} - {self.created_on})"
