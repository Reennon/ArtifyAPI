import os
import shutil
from http import HTTPStatus

from flask import request, flash
from flask_login import current_user
from flask_restful import Resource

from app import db
from constants import Constants
from models.curent_preference import Curent_user_preference
from models.module import Module
from models.preference import Preference
from models.preference_user import Preference_user
from models.preferene_module import Preference_module
from utils.utils import Utils


class UploadModuleResource(Resource):
    """
    POST endpoint handler to save script photo by user
    """

    def post(self):
        """
        Args:
            file from request (flask.request.files['file']): module which send user

        func set file by request and save it on server in Cloud.

        Returns:
            200 OK
        """
        file = request.files['file']
        if not file.filename:
            return flash("None selected script")
        if not Utils.allowed_script_type(filename=file.filename):
            return flash("this image not allowed")
        user_preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        if user_preference_user is None:
            return "please log in "
        curent_preference = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,
                                                             current_user_preference=True).first()
        user_preference = Preference.query.filter_by(id=curent_preference.preference_id).first()
        if not os.path.exists("Cloud"):
            os.mkdir("Cloud")

        if not os.path.exists("Cloud\\Preference_user_" + str(current_user.id)):
            os.mkdir("Cloud\\Preference_user_" + str(current_user.id))
        if not os.path.isdir("Cloud\\Preference_user_" + str(current_user.id) + "\\" + str(curent_preference.name)):
            os.mkdir("Cloud\\Preference_user_" + str(current_user.id) + "\\" + str(curent_preference.name))
            os.mkdir("Cloud\\Preference_user_" + str(current_user.id) + "\\" + str(curent_preference.name) + "\\Modules")
            os.mkdir("Cloud\\Preference_user_" + str(current_user.id) + "\\" + str(curent_preference.name) + "\\Scripts")
        if not os.path.exists("Preference"):
            os.mkdir("Preference")
            os.mkdir("Preference\\Modules")
            os.mkdir("Preference\\Scripts")
        file.save(os.path.join(Constants.cloud_module_folder_path(current_user, curent_preference), file.filename))
        shutil.copy(Constants.cloud_module_folder_path(current_user, curent_preference) + file.filename,
                    Constants.MODULE_FOLDER_PATH)

        if Module.query.filter_by(file_name=str(
                Constants.cloud_module_folder_path(current_user, curent_preference) + file.filename)).first() is None:
            module = Module(
                file_name=str(Constants.cloud_module_folder_path(current_user, curent_preference) + file.filename))
            db.session.add(module)
            db.session.commit()
            preference_module = Preference_module(module_id=module.id, preference_id=curent_preference.preference_id)
            db.session.add(preference_module)
            db.session.commit()

        return HTTPStatus.OK
