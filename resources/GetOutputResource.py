import os
from http import HTTPStatus
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from constants import Constants
from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from models.user import User
from utils.files import Files


class GetOutputResource(Resource):
    @jwt_required()
    def get(self):
        """POST request which handle Core release folder path

        Args:
            id (int):  User id from DataBase
            request body (string): path tothe Relase folder

        Returns:
            Http response 200

        """
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()
        preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        current_preference = Curent_user_preference.query.filter_by(preference_user_id=preference_user.id,
                                                         current_user_preference=True).first()
        file_name= Constants.cloud_folder_path(current_user,current_preference) + 'output.txt'
        file_not_exist = True
        output=""
        while file_not_exist:
            try:
                if os.path.exists(file_name):
                    try:
                        os.rename(file_name, file_name)
                    except:
                        continue
                    file = open(file_name, 'r+')
                    output = file.read()
                    file.close()
                    os.remove(file_name)
                    return output

            except:
                pass

        return HTTPStatus.BadRequest
