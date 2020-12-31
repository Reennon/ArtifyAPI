from app import db


class Preference_file(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    preference_id = db.Column(db.Integer, db.ForeignKey('preference.id'), nullable=False)
    file_id = db.Column(db.Integer, db.ForeignKey('file.id'), nullable=False)
