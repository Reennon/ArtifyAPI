from app import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True , nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(50), nullable=False)
