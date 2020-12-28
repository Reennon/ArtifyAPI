from http import HTTPStatus

from flask import request
from flask_restful import Resource
from constants import Constants
from flask_login import current_user
import shutil

from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user

import os
class NewBuildResource(Resource):

    def post(self,id):

        data = request.get_data().decode()
        path = str(data).replace("\\", "/")

        preference_user = Preference_user.query.filter_by(user_id=id).first()
        current_preference = Curent_user_preference.query.filter_by(preference_user_id=preference_user.id,current_user_preference=True).first()

        if not os.path.exists("Cloud\\Preference_user_" + str(id) + "\\" + str(current_preference.name) + "\\Release\\"):
            os.mkdir("Cloud\\Preference_user_" + str(id) + "\\" + str(current_preference.name) + "\\Release\\")
        shutil.copytree(path, "Cloud\\Preference_user_" + str(id) + "\\" + str(current_preference.name) + "\\Release\\" , dirs_exist_ok=True)
        print(f"for user with id {id}", str(path))
        return HTTPStatus.OK
