import os
import shutil

from flask import request
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
from models.preference_resources import Preference_resource
from models.resources import Resources
class SwitchPreference(Resource):

    def post(self):
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
        module_location = "Preference\\Modules\\"
        script_location = "Preference\\Scripts\\"
        resource_location = "Preference\\Resources\\"
        moddules = os.listdir(os.path.abspath("Preference\\Modules"))
        scripts = os.listdir(os.path.abspath("Preference\\Scripts"))
        resources = os.listdir(os.path.abspath("Preference\\Resources"))
        print('-'*50)
        for script in scripts:
            print("DELETE", script_location + script)
            os.remove(script_location + script)

        for module in moddules:
            print("DELETE", module_location + module)
            os.remove(module_location + module)
        for resurce in resources:
            print("DELETE", resource_location + resurce)
            os.remove(resource_location + resurce)
        user_Preference_modules = Preference_module.query.filter_by(preference_id=new_preference.preference_id)
        user_Preference_script = Preference_script.query.filter_by(preference_id=new_preference.preference_id)
        user_preference_resource = Preference_resource.query.filter_by(preference_id=new_preference.preference_id)
        for preference_module in user_Preference_modules:
            module = Module.query.filter_by(id=preference_module.module_id).first()
            if module is None:
                break
            print("DOWNLOAD >>>", module.file_name)
            shutil.copy(module.file_name, Constants.MODULE_FOLDER_PATH)

        for preference_resource in user_preference_resource:
            resource = Resources.query.filter_by(id=preference_resource.resource_id).first()
            if resource is None:
                break
            print("DOWNLOAD >>>", resource.file_name)
            shutil.copy(resource.file_name, Constants.RESOURCE_FOLDER_PATH)

        for preference_script in user_Preference_script:
            script = Script.query.filter_by(id=preference_script.script_id).first()
            if script is None:
                break
            print("DOWNLOAD >>>", script.file_name)
            shutil.copy(script.file_name, Constants.SCRIPT_FOLDER_PATH)
        print('-' * 50)
        return 200
