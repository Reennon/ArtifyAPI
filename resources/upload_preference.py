import os
import shutil

from flask import send_file
from flask_jwt_extended import get_jwt_identity, jwt_required

from flask_restful import Resource

from constants import Constants
from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from utils.files import Files
from models.user import User

class UpLoadPreferenceResource(Resource):
    @jwt_required()
    def get(self, name):
        """GET method send user his preference by preference nme

        Args:
            name (string): Name of user preference which user want download

        Returns:
            zipped preference file
            http response OK 200

        """
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()
        preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        user_preferences = Curent_user_preference.query.filter_by(preference_user_id=preference_user.id,
                                                                  name=name).first()
        print(user_preferences)
        Files.check_buffer(current_user, user_preferences.name, name)
        shutil.copytree(Constants.cloud_folder_path(current_user, user_preferences),
                        "Buffer\\Preference_user_" + str(current_user.id) + f"/{name}", dirs_exist_ok=True)
        name_path = os.path.join("Buffer\\Preference_user_" + str(current_user.id), name)

        shutil.make_archive(name_path, 'zip', "Buffer/Preference_user_" + str(current_user.id) + f"/{name}")

        return send_file("Buffer/Preference_user_" + str(current_user.id) + f"/{name}.zip", as_attachment=True)
