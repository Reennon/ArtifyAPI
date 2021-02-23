
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from resources.smoke_resource import SmokeResorces
from flask_migrate import Migrate, MigrateCommand



db = SQLAlchemy()
migrate = Migrate()
def create_app():
    """
    fuction build app

    args:
        config (flask.Config): config: API start configuration
    Returns:
         app (Flask): application
    """

    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/rating_db"
    db.init_app(app)
    migrate.init_app(app, db)
    register_resource(api)

    return app


def register_resource(api):


    """
    Connect to API rotes resources
    args:
        api: API which connect the resources routes
    Returns:
         None
    """
    api.add_resource(SmokeResorces, "/smoke")   # test rotes







class Marks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    DisciplineID = db.Column(db.Integer,db.ForeignKey('disciplines.id'), nullable=False)
    Mark = db.Column(db.Integer,nullable= False)
    Passed = db.Column(db.Boolean, nullable=False)

    def __init__(self, id,disceplineID , mark , passed):
        self.id = id
        self.DisciplineID=disceplineID
        self.Mark =mark
        self.Passed = passed


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    StudentID = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    MarksID = db.Column(db.Integer, db.ForeignKey('marks.id'), nullable=False)

    def __init__(self, id, studentID,marksID):
        self.id = id
        self.StudentID=studentID
        self.MarksID =marksID


class Disciplines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Credits = db.Column(db.Integer, nullable=False)
    DisciplineName = db.Column(db.String(50), nullable=False)

    def __init__(self, id, credits, disciplineName):
        self.id = id
        self.Credits=credits
        self.DisciplineName =disciplineName

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Group = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    FirstName = db.Column(db.String(50), nullable=False)

    def __init__(self, id, group, lastName, firstName):
        self.id = id
        self.Group = group
        self.LastName = lastName
        self.FirstName = firstName

