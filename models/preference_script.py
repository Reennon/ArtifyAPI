from app import db


class Preference_script(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    preference_id = db.Column(db.Integer, db.ForeignKey("preference.id"))
    script_id = db.Column(db.Integer, db.ForeignKey("script.id"))
