import os
import shutil
from http import HTTPStatus

from flask import request, flash
from flask_login import current_user
from flask_restful import Resource

from app import db
from constants import Constants
from models.curent_preference import Curent_user_preference
from models.module import Module
from models.preference_script import Preference_script
from models.preference_user import Preference_user
from models.preferene_module import Preference_module
from models.script import Script
from utils.utils import Utils
from models.preference_resources import Preference_resource
from models.resources import Resources

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

        Utils.check_cloud_folder_structure(current_user, curent_preference)

        file.save(path_f)
        Utils.unzip_folder(path_f, name=name_path)
        if os.path.exists("Buffer\\Preference_user_" + str(current_user.id)+"\\preference"):
            os.rename("Buffer\\Preference_user_" + str(current_user.id)+"\\preference", "Buffer\\Preference_user_" + str(current_user.id)+f"\\{curent_preference.name}")
        files = shutil.copytree(name_path, Constants.cloud_preference_folder_path(current_user), dirs_exist_ok=True)
        print(files)
        script_path = Constants.cloud_script_folder_path(current_user, curent_preference)
        module_path = Constants.cloud_module_folder_path(current_user, curent_preference)
        resource_path = Constants.cloud_resource_folder_path(current_user, curent_preference)
        modules = [f for f in os.listdir(module_path)]
        scrptes = [f for f in os.listdir(script_path)]
        resources = [f for f in os.listdir(resource_path)]
        print(scrptes)



        for script_name in scrptes:
            print(script_path + script_name)
            if Script.query.filter_by(file_name=script_path + script_name).first() is None:
                script = Script(
                    file_name=str(Constants.cloud_script_folder_path(current_user, curent_preference) + script_name))
                db.session.add(script)
                db.session.commit()
                preference_scripte = Preference_script(script_id=script.id,
                                                       preference_id=curent_preference.preference_id)
                db.session.add(preference_scripte)
                print(f"NEW SCRIPT {script_name}")
                db.session.commit()
        for module_name in modules:
            print(module_path + module_name)
            if Module.query.filter_by(file_name=module_path + module_name).first() is None:
                module = Module(
                    file_name=str(Constants.cloud_module_folder_path(current_user, curent_preference) + module_name))
                db.session.add(module)
                db.session.commit()
                preference_module = Preference_module(module_id=module.id,
                                                      preference_id=curent_preference.preference_id)
                db.session.add(preference_module)
                print(f"NEW MODULE {module_name}")
                db.session.commit()
        for resources_name in resources:
            print(resource_path + resources_name)
            if Resources.query.filter_by(file_name=resource_path + resources_name).first() is None:
                resource = Resources(
                    file_name=str(Constants.cloud_resource_folder_path(current_user, curent_preference) + resources_name))
                db.session.add(resource)
                db.session.commit()
                preference_resource = Preference_resource(resource_id=resource.id,
                                                        preference_id=curent_preference.preference_id)
                db.session.add(preference_resource)
                print(f"NEW SCRIPT {resources_name}")
                db.session.commit()
        if os.path.exists(path_f):
            os.remove(path_f)
        if os.path.exists(name_path):
            shutil.rmtree(os.path.join("Buffer\\Preference_user_" + str(current_user.id), name))
        print("delete")


        return HTTPStatus.OK
