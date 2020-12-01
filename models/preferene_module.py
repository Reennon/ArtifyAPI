from app import db


class Preference_module(db.Model):
    id = db.Column(db.Integer,primary_key=True , nullable=False)
    preference_id = db.Column(db.Integer, db.ForeignKey('preference.id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)

