import os
import shutil
from http import HTTPStatus

from flask import request, flash
from flask_login import current_user
from flask_restful import Resource

from app import db
from constants import Constants
from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from utils.files import Files
from utils.utils import Utils


class UploadScriptResource(Resource):
    """
    POST endpoint handler to save script photo by user
    """

    def post(self):
        """
        Args:
            file from request (flask.request.files['file']): script which send user

        func set file by request and save it on server in folder 'data-storage/Script/' and
        send Core message with name of script.

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

        if not os.path.exists("Cloud"):
            os.mkdir("Cloud")
        Files.check_cloud_folder(current_user, curent_preference)
        Files.check_preference()

        file.save(os.path.join(Constants.cloud_script_folder_path(current_user, curent_preference), file.filename))
        shutil.copy(Constants.cloud_script_folder_path(current_user, curent_preference) + file.filename,
                    Constants.SCRIPT_FOLDER_PATH)
        Files.upload_file(current_user,curent_preference,file.filename,db)

        return HTTPStatus.OK
