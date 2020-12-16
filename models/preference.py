from app import db


class Preference(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)

