from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user, login_user

from resources.upload_photo_resource import UploadPhotoResource
from flask_cors import CORS
from constants import Constants
from resources.run_build_resource import RunBuildResource
from resources.update_executable_resource import UpdateExecutableResource

from resources.error_resource import ErrorResource
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity
)


APP_NAME = "Artify"
APP_PREFIX = "/artify"
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()


def create_app(config=None):
    """
    fuction build app

    args:
        config (flask.Config): config: API start configuration
    Returns:
         app (Flask): application
    """

    app = Flask(APP_NAME)
    jwt = JWTManager(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = Constants.SQLALCHEMY_DATABASE_URI
    app.config['SECRET_KEY'] = Constants.SECRET_KEY
    api = Api(app, prefix=APP_PREFIX)
    app.config.from_object(config)
    db.init_app(app)

    from models.preference import Preference
    from models.curent_preference import Curent_user_preference
    from models.file import File
    from models.preference_file import Preference_file
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
    setup_origins_cors(app)

    @app.before_request
    def before_request_auth():
        pass

    return app


def register_resource(api):
    """
    Connect to API rotes resource
    args:
        api: API which connect the resource routes
    Returns:
         None
    """
    from resources.new_build_resource import NewBuildResource
    from resources.switch_preference import SwitchPreference
    from resources.upload_script_resource import UploadScriptResource
    from resources.upload_module_resource import UploadModuleResource
    from resources.build_resource import BuildResource
    from resources.load_preference import LoadPreferenceResource
    from resources.upload_preference import UpLoadPreferenceResource
    from resources.upload_resource import UploadResource
    from resources.smoke_resource import SmokeResorces
    from resources.get_folder_tree_resource import GetFolderTreeResource
    from resources.dropdown_menu_resource import GetUserProjectResource
    from resources.LoginResource import LoginResource
    from resources.UploadScriptByJson import UploadScriptByJsonResource
    from resources.GetOutputResource import GetOutputResource

    api.add_resource(SmokeResorces, "/smoke")  # test rotes GET
    api.add_resource(UploadPhotoResource, "/photo")  # photo upload routes, POST
    api.add_resource(UploadScriptResource, "/script")  # script upload routes, POST
    api.add_resource(RunBuildResource, '/run')  # GET
    api.add_resource(UpdateExecutableResource, '/update')  # POST
    api.add_resource(NewBuildResource, '/new/<int:id>')  # POST
    api.add_resource(BuildResource, '/build')  # GET, POST
    api.add_resource(UploadModuleResource, "/module")  # POST
    api.add_resource(ErrorResource, "/error/<int:id>")  # GET
    api.add_resource(SwitchPreference, "/switch")  # POST
    api.add_resource(LoadPreferenceResource, "/preference")  # GET, POST
    api.add_resource(UpLoadPreferenceResource, "/upload_preference/<string:name>")  # GET
    api.add_resource(UploadResource, "/resources")  # POST
    api.add_resource(GetFolderTreeResource, "/tree")  # GET
    api.add_resource(GetUserProjectResource, "/dropdown")  # GET
    api.add_resource(LoginResource, "/login")  # GET
    api.add_resource(UploadScriptByJsonResource,'/script/json')  #POST
    api.add_resource(GetOutputResource,'/output')   #GET
    # ('/login', methods=['POST'])
    # ('/logout',methods=['GET, POST'])
    # ('/signup', methods={'POST'})


def import_bluprint_resource():
    from resources.auth.signup import signup



def setup_origins_cors(api):
    """
    Setups cors origins from consts
    Args:
        api:
    Returns:
        None:
    """
    from constants import Constants as Const
    CORS(api, origins=[r"http://localhost:5000", r"https://localhost:5001", r"http://192.168.0.104:5000"])
