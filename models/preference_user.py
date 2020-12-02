from app import db


class Preference_user(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    preference_id = db.Column(db.Integer, db.ForeignKey("preference.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
