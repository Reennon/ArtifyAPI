import os
import shutil

from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_login import current_user
from flask_restful import Resource

from app import db
from constants import Constants
from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from models.user import User

class SwitchPreference(Resource):
    @jwt_required()
    def post(self):
        """
        Args:
            request body (json):
                                {
                                    "name":"Artify" // Preference name which user want switched
                                }
        Returns:
            Http response OK 200
        """
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()
        data = request.get_json()
        preference_name = data['name']
        user_preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        if user_preference_user is None:
            return "please log in "

        if not os.path.exists("Cloud"):
            os.mkdir("Cloud")
        new_preference = Curent_user_preference.query.filter_by(name=preference_name,
                                                                preference_user_id=user_preference_user.id).first()
        old_preference = Curent_user_preference.query.filter_by(current_user_preference=True,
                                                                preference_user_id=user_preference_user.id).first()
        old_preference.current_user_preference = False
        new_preference.current_user_preference = True
        db.session.commit()

        print('-' * 50)
        shutil.rmtree(Constants.PREFERENCE_PATH)
        shutil.copytree(Constants.cloud_folder_path(current_user, new_preference), Constants.PREFERENCE_PATH,
                        dirs_exist_ok=True)

        print('-' * 50)
        return 200
