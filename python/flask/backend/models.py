from . import db
from flask_login import UserMixin


class todo(db.Model):
    title = db.Column(db.String(350))
    completed = db.Column(db.Boolean, default=False)

class User(db.Model):
    name = db.Column(db.Text)