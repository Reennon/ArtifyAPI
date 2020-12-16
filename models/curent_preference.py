from app import db


class Curent_user_preference(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    preference_id = db.Column(db.Integer, db.ForeignKey("preference.id"))
    preference_user_id = db.Column(db.Integer, db.ForeignKey("preference_user.id"))
    current_user_preference = db.Column(db.Boolean, nullable=False)
    name = db.Column(db.String(50), nullable=False)