from http import HTTPStatus
from flask import request
from flask_restful import Resource
from flask_login import current_user
from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from utils.socket_connect import SocketConnection
from constants import Constants

class RunBuildResource(Resource):
    """
    POST send Core command build project
    GET get from Core Build DLL from project
    """

    def get(self):

        json = request.get_json()
        query = json.get(None, json["Query"])
        preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()


        current_preference = Curent_user_preference.query.filter_by(preference_user_id=preference_user.id,
                                                                    current_user_preference=True).first()

        import os
        return os.path.abspath(Constants.cloud_folder_path(current_user,current_preference)+f"\\Release\\{query}.dll")

    def post(self):

        return int(current_user.id)
