import shutil
from http import HTTPStatus

from flask import flash
from flask import request
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash
from app import db
from auth.auth import auth
from constants import Constants
from models.curent_preference import Curent_user_preference
from models.module import Module
from models.preference import Preference
from models.preference_script import Preference_script
from models.preference_user import Preference_user
from models.preferene_module import Preference_module
from models.preference_resources import Preference_resource
from models.resources import Resources
from models.user import User
from models.script import Script

@auth.route('/login', methods=['POST'])
def login():
    """
    POST method

    Point:
        Logging in user and manage his folders on cloud to local

    Args:
        request body (json):
                            {
                                "preference_name":"Artify",
                                "password":"s",
                                "email":"s@s.com"
                            }

    Returns:
        string: <hello {username}, welcome on {preference_name}>
        response OK 200

    """
    data = request.get_json()
    password = data['password']
    email = data['email']
    preference_name = data['preference_name']

    user = User.query.filter_by(email=email).first()

    if not user and not check_password_hash(user.password, password):
        flash("wrong password or email ")
        return HTTPStatus.BAD_REQUEST
    if current_user.email is user.email:
        return "you already logged in "
    user_preference_user = Preference_user.query.filter_by(user_id=user.id).first()
    if preference_name is None:
        current_preference = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,
                                                                current_user_preference=True).first()
    else:
        current_preference = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,
                                                                    name=preference_name).first()
        old_current = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,
                                                             current_user_preference=True).first()
        old_current.current_user_preference = False

        print(f" preference_user  {user_preference_user.id}\n"
              f" preference_user  {preference_name}")
        if current_preference is None:



            new_preference = Preference()
            db.session.add(new_preference)
            db.session.commit()
            current_preference = Curent_user_preference(current_user_preference=True,
                                                            name=preference_name,
                                                            preference_user_id=user_preference_user.id,
                                                            preference_id=new_preference.id)

            db.session.add(current_preference)
        current_preference.current_user_preference = True
        print(f" preference_user  {user_preference_user.id}\n"
              f" preference_user  {current_preference.name}")
        db.session.commit()
    user_preference = Preference.query.filter_by(id=current_preference.preference_id).first()

    user_Preference_modules = Preference_module.query.filter_by(preference_id=user_preference.id)
    user_Preference_resource = Preference_resource.query.filter_by(preference_id=user_preference.id)
    user_Preference_script = Preference_script.query.filter_by(preference_id=user_preference.id)

    login_user(user)

    for preference_module in user_Preference_modules:
        module = Module.query.filter_by(id=preference_module.module_id).first()
        print("DOWNLOAD >>>", module.file_name)
        shutil.copy(module.file_name, Constants.MODULE_FOLDER_PATH)

    for preference_resource in user_Preference_resource:
        res = Resources.query.filter_by(id=preference_resource.resource_id).first()
        print("DOWNLOAD >>>", res.file_name)
        shutil.copy(res.file_name, Constants.RESOURCE_FOLDER_PATH)

    for preference_script in user_Preference_script:
        script = Script.query.filter_by(id=preference_script.script_id).first()
        print("DOWNLOAD >>>", script.file_name)
        shutil.copy(script.file_name, Constants.SCRIPT_FOLDER_PATH)
    return f"hello {user.username}, welcome on {preference_name}"
