import os
import shutil
from http import HTTPStatus

from flask import request, flash
from flask_jwt_extended import get_jwt_identity, jwt_required

from flask_restful import Resource

from app import db
from constants import Constants
from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from utils.files import Files
from models.user import User

class UploadResource(Resource):
    @jwt_required()
    def post(self):
        """
                Args:
                    file from request (flask.request.files['file']): resource which send user

                func set file by request and save it on server in Cloud.

                Returns:
                    200 OK
                """
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()
        file = request.files['file']
        if not file.filename:
            return flash("None selected resource")
        user_preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        if user_preference_user is None:
            return "please log in "
        curent_preference = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,
                                                                   current_user_preference=True).first()

        Files.check_cloud_folder(current_user,curent_preference)
        Files.check_preference()
        file.save(os.path.join(Constants.cloud_resource_folder_path(current_user, curent_preference), file.filename))
        shutil.copy(Constants.cloud_resource_folder_path(current_user, curent_preference) + file.filename,
                    Constants.RESOURCE_FOLDER_PATH)

        Files.upload_file(current_user, curent_preference, file.filename, db)
        return HTTPStatus.OK
