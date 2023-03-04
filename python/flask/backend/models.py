from . import db

class todo(db.Model):
    title = db.Column(db.String(350))
    completed = db.Column(db.Boolean, default=False)

class User(db.Model):
    name = db.Column(db.Text)