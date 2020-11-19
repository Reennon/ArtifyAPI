from flask import Flask
from flask_restful import Api
from ArtifyAPI.resources.smoke_resource import SmokeResorces
from ArtifyAPI.resources.upload_photo_resource import UploadPhotoResource


APP_NAME = "Artify"
APP_PREFIX = "/Artify"

def create_app(config=None):
    """
    fuction build app

    args:
        config (flask.Config): config: API start configuration
    Returns:
         app (Flask): application
    """


    app = Flask(APP_NAME)
    api = Api(app,prefix=APP_PREFIX)
    app.config.from_object(config)
    app.logger_name = APP_NAME

    register_resource(api)

    return app


def register_resource(api):
    """
    Connect to API rotes resource
    args:
        api: API which connect the resource Smoke, photo upload
    Returns:
         None
    """
    api.add_resource(SmokeResorces, "/smoke")
    api.add_resource(UploadPhotoResource, "/photo")
