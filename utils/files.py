import os
import shutil

from flask_login import login_user

from constants import Constants
from models.curent_preference import Curent_user_preference
from models.module import Module
from models.preference import Preference
from models.preference_resources import Preference_resource
from models.preference_script import Preference_script
from models.preference_user import Preference_user
from models.preferene_module import Preference_module
from models.resources import Resources
from models.script import Script


class Files:
    @staticmethod
    def get_full_path(path):
        return os.path.abspath(path)

    @staticmethod
    def standart_dir():
        root_dir = ["Modules", "Scripts", "Resources"]
        return root_dir

    @staticmethod
    def check_cloud_folder(current_user, curent_preference, ):
        if not os.path.exists("Cloud\\Preference_user_" + str(current_user.id)):
            os.mkdir("Cloud\\Preference_user_" + str(current_user.id))
        if not os.path.isdir("Cloud\\Preference_user_" + str(current_user.id) + "\\" + str(curent_preference.name)):
            os.mkdir("Cloud\\Preference_user_" + str(current_user.id) + "\\" + str(curent_preference.name))
            for dir in Files.standart_dir():
                os.mkdir(
                    "Cloud\\Preference_user_" + str(current_user.id) + "\\" + str(curent_preference.name) + f"\\{dir}")
        if not os.path.exists("Preference"):
            os.mkdir("Preference")
            for dir in Files.standart_dir():
                os.mkdir(f"Preference\\{dir}")

    @staticmethod
    def prepear_to_login(user, preference_name, db):

        user_preference_user = Preference_user.query.filter_by(user_id=user.id).first()
        if preference_name is None:
            current_preference = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,
                                                                        current_user_preference=True).first()
        else:
            current_preference = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,
                                                                        name=preference_name).first()
            old_current = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,
                                                                 current_user_preference=True).first()
            old_current.current_user_preference = False

            print(f" preference_user  {user_preference_user.id}\n"
                  f" preference_user  {preference_name}")
            if current_preference is None:
                new_preference = Preference()
                db.session.add(new_preference)
                db.session.commit()
                current_preference = Curent_user_preference(current_user_preference=True,
                                                            name=preference_name,
                                                            preference_user_id=user_preference_user.id,
                                                            preference_id=new_preference.id)

                db.session.add(current_preference)
            current_preference.current_user_preference = True
            print(f" preference_user  {user_preference_user.id}\n"
                  f" preference_user  {current_preference.name}")
            db.session.commit()
        login_user(user)
        shutil.copytree(Files.get_full_path(Constants.cloud_folder_path(user, current_preference)),
                        Constants.PREFERENCE_PATH, dirs_exist_ok=True)

    @staticmethod
    def prepear_to_logout():
        module_location = "...\\..\\Preference\\Modules\\"
        script_location = "...\\..\\Preference\\Scripts\\"
        moddules = os.listdir(os.path.abspath("...\\..\\Preference\\Modules"))
        scripts = os.listdir(os.path.abspath("...\\..\\Preference\\Scripts"))
        for script in scripts:
            print("DELETE", script_location + script)
            os.remove(script_location + script)

        for module in moddules:
            print("DELETE", module_location + module)
            os.remove(module_location + module)

    @staticmethod
    def check_buffer(current_user, filename, name):
        if not os.path.exists("Buffer"):
            os.mkdir("Buffer")
        if not os.path.exists("Buffer\\Preference_user_" + str(current_user.id)):
            os.mkdir("Buffer\\Preference_user_" + str(current_user.id))
        path_f = os.path.join("Buffer\\Preference_user_" + str(current_user.id), filename)
        if os.path.exists(path_f):
            os.remove(path_f)
        name_path = os.path.join("Buffer\\Preference_user_" + str(current_user.id), name)
        if os.path.exists(name_path):
            shutil.rmtree(name_path)

    @staticmethod
    def Upload_to_cloud(current_user, curent_preference, db, name_path):
        if os.path.exists("Buffer\\Preference_user_" + str(current_user.id) + "\\preference"):
            os.rename("Buffer\\Preference_user_" + str(current_user.id) + "\\preference",
                      "Buffer\\Preference_user_" + str(current_user.id) + f"\\{curent_preference.name}")
        shutil.copytree(name_path, Constants.cloud_preference_folder_path(current_user), dirs_exist_ok=True)

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
                    file_name=str(
                        Constants.cloud_resource_folder_path(current_user, curent_preference) + resources_name))
                db.session.add(resource)
                db.session.commit()
                preference_resource = Preference_resource(resource_id=resource.id,
                                                          preference_id=curent_preference.preference_id)
                db.session.add(preference_resource)
                print(f"NEW RESOURCE {resources_name}")
                db.session.commit()

    @staticmethod
    def update_db(current_user, curent_preference):

        pass
