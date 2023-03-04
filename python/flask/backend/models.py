from . import db
from flask_login import UserMixin


class todo(db.Model):
    id - db.Column(db.integer, primary_key=True)
    title = db.Column(db.String(350))
    completed = db.Column(db.Boolean, default=False)

class User(db.Model, UserMixin):

    name = db.Column(db.Text)