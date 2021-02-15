import os
import shutil
from http import HTTPStatus

from flask import request, flash
from flask_jwt_extended import jwt_required, get_jwt_identity

from flask_restful import Resource

from app import db
from constants import Constants
from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from utils.files import Files
from utils.utils import Utils
from models.user import User

class LoadPreferenceResource(Resource):
    @jwt_required()
    def get(self):
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()
        preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        user_preferences = Curent_user_preference.query.filter_by(preference_user_id=preference_user.id)
        print(user_preferences)
        preferences = [preference.name for preference in user_preferences]
        return {
            "preferences": preferences
        }

    def post(self):
        """POST method
            func set file by request and save it on Buffer then unzipped it
            and synchronization new and update files and

        Args:
            file from request (flask.request.files['file']): Zipped preference  which send user

        Returns:
            200 OK
        """

        file = request.files['file']
        if not file.filename:
            return flash("None selected script")
        if not file.filename.endswith(".zip"):
            return flash("this image not allowed")
        user_preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        curent_preference = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,
                                                                   current_user_preference=True).first()
        name = file.filename.split('.')[0]
        name_path = os.path.join("Buffer\\Preference_user_" + str(current_user.id), os.path.join(curent_preference.name))
        path_f = os.path.join("Buffer\\Preference_user_" + str(current_user.id),  curent_preference.name+".zip")
        Files.check_buffer(current_user, curent_preference.name, name)
        Files.check_cloud_folder_structure(current_user, curent_preference)

        file.save(path_f)
        Utils.unzip_folder(path_f, name=name_path)
        Files.Upload_to_cloud(current_user, curent_preference, db, os.path.join(name_path, name))

        shutil.copytree(Constants.cloud_folder_path(current_user, curent_preference), Constants.PREFERENCE_PATH,
                        dirs_exist_ok=True)

        if os.path.exists(path_f):
            os.remove(path_f)
        if os.path.exists(name_path):
            shutil.rmtree(os.path.join("Buffer\\Preference_user_" + str(current_user.id)))

        return HTTPStatus.OK
