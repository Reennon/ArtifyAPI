from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from ArtifyAPI.resources.SmokeResource import SmokeResorces
from ArtifyAPI.settings.settings import Config

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

