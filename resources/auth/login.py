from http import HTTPStatus
import shutil
from flask import flash
from flask import request
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash

from auth.auth import auth
from models.user import User
from models.preference_user import Preference_user
from models.preference import Preference
from models.preferene_module import Preference_module
from models.module import Module
from constants import Constants
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    password = data['password']
    email = data['email']

    user = User.query.filter_by(email=email).first()
    if not user and not check_password_hash(user.password, password):
        flash("wrong password or email ")
        return HTTPStatus.BAD_REQUEST
    if current_user.email is user.email:
        return "you already logged in "

    login_user(user)
    print()
    user_preference_user = Preference_user.query.filter_by(user_id= user.id).first()
    user_preference = Preference.query.filter_by(id =user_preference_user.preference_id).first()
    user_Preference_modules = Preference_module.query.filter_by(preference_id= user_preference.id)
    for preference_module in user_Preference_modules:
        module= Module.query.filter_by(id=preference_module.module_id).first()
        print("DOWNLOAD >>>",module.file_name)
        shutil.copy(module.file_name, Constants.MODULE_FOLDER_PATH )
    return f"hello {user.username}, welcome on {user_preference.name}"
