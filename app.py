from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from resources.smoke_resource import SmokeResorces
from resources.upload_photo_resource import UploadPhotoResource
from resources.upload_script_resource import UploadScriptResource

APP_NAME = "Artify"
APP_PREFIX = "/Artify"
db = SQLAlchemy()
migrate = Migrate()


def create_app(config=None):
    """
    fuction build app

    args:
        config (flask.Config): config: API start configuration
    Returns:
         app (Flask): application
    """

    app = Flask(APP_NAME)
    api = Api(app, prefix=APP_PREFIX)
    app.config.from_object(config)
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/artify_db"
    migrate.init_app(app, db)
    app.logger_name = APP_NAME

    register_resource(api)

    return app


def register_resource(api):
    """
    Connect to API rotes resource
    args:
        api: API which connect the resource routes
    Returns:
         None
    """
    api.add_resource(SmokeResorces, "/smoke")  # test rotes
    api.add_resource(UploadPhotoResource, "/photo")  # photo upload routes
    api.add_resource(UploadScriptResource, "/script")  # script upload routes
