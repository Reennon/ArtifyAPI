from flask import Flask
from flask_restful import Api
from resources.smoke_resource import SmokeResorces
from resources.upload_photo_resource import UploadPhotoResource
from resources.upload_script_resource import UploadScriptResource
from resources.build_resource import BuildResource
from resources.run_module_resource import ModuleResource
from resources.update_executable_resource import UpdateExecutableResource

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
        api: API which connect the resource routes
    Returns:
         None
    """
    api.add_resource(SmokeResorces, "/smoke")   # test rotes
    api.add_resource(UploadPhotoResource, "/photo")    # photo upload routes
    api.add_resource(UploadScriptResource, "/script")   # script upload routes
    api.add_resource(BuildResource,"/build")
    api.add_resource(ModuleResource,"/module")
    api.add_resource(UpdateExecutableResource,'/python')


