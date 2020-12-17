
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user, login_user
from resources.smoke_resource import SmokeResorces
from resources.upload_photo_resource import UploadPhotoResource

from resources.run_build_resource import RunBuildResource
from resources.update_executable_resource import UpdateExecutableResource
from resources.new_build_resource import NewBuildResource
from resources.error_resource import ErrorResource

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
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/artify_db"
    app.config['SECRET_KEY'] = 'stepan'
    api = Api(app, prefix=APP_PREFIX)
    app.config.from_object(config)
    db.init_app(app)

    from models.preference import Preference
    from models.preference_script import Preference_script
    from models.preferene_module import Preference_module
    from models.module import Module
    from models.script import Script
    from models.curent_preference import Curent_user_preference
    from models.user import User
    from models.preference_user import Preference_user

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(int(user_id))

    migrate.init_app(app, db)

    app.logger_name = APP_NAME
    from auth.auth import auth as auth_blueprint
    import_bluprint_resource()
    app.register_blueprint(auth_blueprint)

    register_resource(api)

    @app.before_request
    def before_request_auth():
        if not current_user.is_authenticated:
            user = User.query.filter_by(email="user").first()
            login_user(user)
    return app


def register_resource(api):
    """
    Connect to API rotes resource
    args:
        api: API which connect the resource routes
    Returns:
         None
    """
    from resources.switch_preference import SwitchPreference
    from resources.upload_script_resource import UploadScriptResource
    from resources.upload_module_resource import UploadModuleResource
    from resources.build_resource import BuildResource
    from resources.load_preference import LoadPreferenceResource
    api.add_resource(SmokeResorces, "/smoke")  # test rotes
    api.add_resource(UploadPhotoResource, "/photo")  # photo upload routes
    api.add_resource(UploadScriptResource, "/script")  # script upload routes
    api.add_resource(RunBuildResource, '/run')
    api.add_resource(UpdateExecutableResource, '/update')
    api.add_resource(NewBuildResource, '/new/<int:id>')
    api.add_resource(BuildResource, '/build')
    api.add_resource(UploadModuleResource, "/module")
    api.add_resource(ErrorResource, "/error/<int:id>")
    api.add_resource(SwitchPreference, "/switch")
    api.add_resource(LoadPreferenceResource, "/load")

def import_bluprint_resource():
    from resources.auth.login import login
    from resources.auth.signup import signup
    from resources.auth.logout import logout
