import os
import sys
from http import HTTPStatus
from flask import request
from flask_restful import Resource
from constants import Constants
from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from models.user import User
from utils.files import Files

class NewBuildResource(Resource):

    def post(self, id):
        """POST request which handle Core release folder path

        Args:
            id (int):  User id from DataBase
            request body (string): path tothe Relase folder

        Returns:
            Http response 200

        """

        current_user = User.query.filter_by(id=id).first()
        preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        current_preference = Curent_user_preference.query.filter_by(preference_user_id=preference_user.id,
                                                                    current_user_preference=True).first()
        data = request.get_data()
        path = str(data).replace('\\\\','\\')
        code, out, err = Files.run(["dotnet", path[2:-1]])
        path_to_output= Constants.cloud_folder_path(current_user,current_preference) + 'output.txt'
        file = open(path_to_output,'w+')
        file.write(str(out))
        file.close()

        print(f"for user with id {id}", str(path))
        return HTTPStatus.OK
