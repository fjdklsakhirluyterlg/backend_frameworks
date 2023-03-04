from . import db
from flask_login import UserMixin
from datetime import datetime


class todo(db.Model):
    id - db.Column(db.integer, primary_key=True)
    title = db.Column(db.String(350))
    completed = db.Column(db.Boolean, default=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(50))