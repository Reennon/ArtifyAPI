from app import db


class Preference_resource(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    preference_id = db.Column(db.Integer, db.ForeignKey('preference.id'), nullable=False)
    resource_id = db.Column(db.Integer, db.ForeignKey('resources.id'), nullable=False)
