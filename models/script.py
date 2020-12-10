from app import db


class Script(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
