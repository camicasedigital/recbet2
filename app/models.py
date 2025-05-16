from . import db

class Bet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question1 = db.Column(db.String(100))
    question2 = db.Column(db.String(100))
    question3 = db.Column(db.String(100))
