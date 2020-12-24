import os
import shutil
from http import HTTPStatus

from flask import request, flash
from flask_login import current_user
from flask_restful import Resource
import zipstream
from constants import Constants
from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from flask import send_file, send_from_directory, make_response
from utils.utils import Utils


class UpLoadPreferenceResource(Resource):
    def get(self,name):
        """GET method send user his preference by preference nme

        Args:
            name (string): Name of user preference which user want download

        Returns:
            zipped preference file
            http response OK 200

        """
        if not os.path.exists("Buffer"):
            os.mkdir("Buffer")
        if not os.path.exists("Buffer\\Preference_user_" + str(current_user.id)):
            os.mkdir("Buffer\\Preference_user_" + str(current_user.id))
        if os.path.exists("Buffer/Preference_user_" + str(current_user.id)+ f"/{name}"):
            shutil.rmtree("Buffer/Preference_user_" + str(current_user.id) + f"/{name}")
            os.remove("Buffer/Preference_user_" + str(current_user.id) + f"/{name}.zip")
        preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        user_preferences = Curent_user_preference.query.filter_by(preference_user_id=preference_user.id,name=name).first()
        print(user_preferences)

        shutil.copytree(Constants.cloud_folder_path(current_user,user_preferences),"Buffer\\Preference_user_" + str(current_user.id)+ f"/{name}", dirs_exist_ok=True)
        name_path = os.path.join("Buffer\\Preference_user_" + str(current_user.id), name)

        shutil.make_archive(name_path, 'zip', "Buffer/Preference_user_" + str(current_user.id)+f"/{name}")


        return send_file("Buffer/Preference_user_" + str(current_user.id)+f"/{name}.zip" , as_attachment=True)
