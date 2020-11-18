from flask import Flask
from flask_restful import Api
from ArtifyAPI.resources.SmokeResource import SmokeResorces
from ArtifyAPI.resources.UploadPhotoResource import UploadPhotoResource


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

    register_smoke_rotes(api)
    register_upload_photo_rotes(api)

    return app


def register_smoke_rotes(api):
    """
    Connect to API resource Smoke
    args:
        api: API which connect the resource Smoke
    Returns:
         None
    """
    api.add_resource(SmokeResorces, "/smoke")

def register_upload_photo_rotes(api):
    """
        Connect to API resource photo upload
        args:
            api: API which connect the resource photo upload
        Returns:
             None
        """
    api.add_resource(UploadPhotoResource, "/photo")