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
from models.preference_script import Preference_script
from models.preference_user import Preference_user
from models.preferene_module import Preference_module
from models.script import Script
from utils.utils import Utils
from models.preference_resources import Preference_resource
from models.resources import Resources
from utils.files import Files
class LoadPreferenceResource(Resource):
    def get(self):
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
        name_path = os.path.join("Buffer\\Preference_user_" + str(current_user.id), name)
        path_f = os.path.join("Buffer\\Preference_user_" + str(current_user.id), file.filename)
        Files.check_buffer(current_user,file.filename,name)
        print("Create")

        Utils.check_cloud_folder_structure(current_user, curent_preference)

        file.save(path_f)

        Utils.unzip_folder(path_f, name=name_path)

        Files.Upload_to_cloud(current_user, curent_preference,db,name_path)



        if os.path.exists(path_f):
            os.remove(path_f)
        if os.path.exists(name_path):
            shutil.rmtree(os.path.join("Buffer\\Preference_user_" + str(current_user.id), name))
        print("delete")


        return HTTPStatus.OK
