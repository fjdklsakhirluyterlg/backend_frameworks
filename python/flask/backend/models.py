from . import db

class todo(db.Model):
    title = db.Column(db.String(350))