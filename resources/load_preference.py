import os
import shutil
from http import HTTPStatus

from flask import request, flash
from flask_login import current_user
from flask_restful import Resource

from constants import Constants
from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from utils.utils import Utils


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
        if not file.filename.endswith(".zip"):
            return flash("this image not allowed")
        user_preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        curent_preference = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,
                                                                   current_user_preference=True).first()
        if not os.path.exists("Buffer"):
            os.mkdir("Buffer")
        name = file.filename.split('.')[0]
        if not os.path.exists("Buffer\\Preference_user_" + str(current_user.id)):
            os.mkdir("Buffer\\Preference_user_" + str(current_user.id))
        path_f = os.path.join("Buffer\\Preference_user_" + str(current_user.id), file.filename)
        if os.path.exists(path_f):
            os.remove(path_f)
        name_path = os.path.join("Buffer\\Preference_user_" + str(current_user.id), name)
        if os.path.exists(name_path):
            shutil.rmtree(name_path)
        print("Create")

        file.save(path_f)

        Utils.unzip_folder(path_f, name=name_path)
        shutil.copytree(name_path, Constants.cloud_preference_folder_path(current_user), dirs_exist_ok=True)
        print("delete")
        if os.path.exists(path_f):
            os.remove(path_f)
        if os.path.exists(name_path):
            shutil.rmtree(os.path.join("Buffer\\Preference_user_" + str(current_user.id), name))

        """


        user_preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        if user_preference_user is None:
            return "please log in "
        curent_preference = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,
                                                             current_user_preference=True).first()
        user_preference = Preference.query.filter_by(id=curent_preference.preference_id).first()
        if not os.path.exists("Bufer"):
            os.mkdir("Bufer")

        if not os.path.exists("Bufer\\Preference_user_" + str(current_user.id)):
            os.mkdir("Bufer\\Preference_user_" + str(current_user.id))
        if not os.path.isdir("Bufer\\Preference_user_" + str(current_user.id) + "\\" + str(curent_preference.name)):
            os.mkdir("Bufer\\Preference_user_" + str(current_user.id) + "\\" + str(curent_preference.name))
            os.mkdir("Bufer\\Preference_user_" + str(current_user.id) + "\\" + str(curent_preference.name) + "\\Modules")
            os.mkdir("Bufer\\Preference_user_" + str(current_user.id) + "\\" + str(curent_preference.name) + "\\Scripts")
        if not os.path.exists("Preference"):
            os.mkdir("Preference")
            os.mkdir("Preference\\Modules")
            os.mkdir("Preference\\Scripts")
        file.save(os.path.join(Constants.cloud_script_folder_path(current_user, curent_preference), file.filename))
        shutil.copy(Constants.cloud_script_folder_path(current_user, curent_preference) + file.filename,
                    Constants.SCRIPT_FOLDER_PATH)

        if Script.query.filter_by(file_name=str(
                Constants.cloud_script_folder_path(current_user, curent_preference) + file.filename)).first() is None:
            script = Script(
                file_name=str(Constants.cloud_script_folder_path(current_user, curent_preference) + file.filename))
            db.session.add(script)
            db.session.commit()
            preference_module = Preference_script(script_id=script.id, preference_id=curent_preference.preference_id)
            db.session.add(preference_module)
            db.session.commit()"""

        return HTTPStatus.OK
