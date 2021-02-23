import os
import shutil
import subprocess

from flask_jwt_extended import create_access_token
from flask_login import login_user

from constants import Constants
from models.curent_preference import Curent_user_preference
from models.file import File
from models.preference import Preference
from models.preference_file import Preference_file
from models.preference_user import Preference_user


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
        access_token = create_access_token(identity=user.username, expires_delta=False)
        Files.check_cloud_folder(user,current_preference)
        shutil.copytree(Files.get_full_path(Constants.cloud_folder_path(user, current_preference)),
                        Constants.PREFERENCE_PATH, dirs_exist_ok=True)
        return {"token": 'Bearer '+access_token}
    @staticmethod
    def get_all_files_from_db_by_user_preference(preference_id):
        pref_files = Preference_file.query.filter_by(preference_id=preference_id)

        all_files = [[file.file_name for file  in  File.query.filter_by(id= pref.file_id)] for pref in pref_files]

        return all_files


    @staticmethod
    def prepear_to_logout():
        shutil.rmtree(Constants.PREFERENCE_PATH)

    @staticmethod
    def check_buffer(current_user, filename, name):
        if not os.path.exists("Buffer"):
            os.mkdir("Buffer")
        if not os.path.exists("Buffer\\Preference_user_" + str(current_user.id)):
            os.mkdir("Buffer\\Preference_user_" + str(current_user.id))
        path_f = os.path.join("Buffer\\Preference_user_" + str(current_user.id), filename)
        if os.path.exists(path_f):
            shutil.rmtree(path_f)
        name_path = os.path.join("Buffer\\Preference_user_" + str(current_user.id), name)
        if os.path.exists(name_path):
            shutil.rmtree(name_path)

    @staticmethod
    def Upload_to_cloud(current_user, curent_preference, db, name_path):
        if os.path.exists("Buffer\\Preference_user_" + str(current_user.id) + "\\preference"):
            os.rename("Buffer\\Preference_user_" + str(current_user.id) + "\\preference",
                      "Buffer\\Preference_user_" + str(current_user.id) + f"\\{curent_preference.name}")
        shutil.copytree(name_path, Constants.cloud_folder_path(current_user,curent_preference), dirs_exist_ok=True)

        all_files = Files.get_files_from_cloud(current_user, curent_preference)

        for path in all_files:
            if File.query.filter_by(file_name=path).first() is None:
                file = File(file_name=path)
                db.session.add(file)
                db.session.commit()
                preference_file = Preference_file(file_id=file.id,
                                                       preference_id=curent_preference.preference_id)
                db.session.add(preference_file)
                print(f"NEW File {path}")
                db.session.commit()
            else:
                print(f"Update File {path}")


    @staticmethod
    def update_db(user,current_preference):
        all_files = Files.get_all_files_from_db_by_user_preference(current_preference.preference_id)
        db_files = [ str(file[0]).replace(Constants.cloud_folder_path(user,current_preference),"") for file in all_files]

        exist = [path.replace(Constants.cloud_folder_path(user,current_preference), "") for path in Files.get_files_from_cloud(user,current_preference)]
        print(db_files)
        print(exist)
        not_exist = []
        for file in exist:
            if file in db_files:
                db_files.remove(file)
            else:
                not_exist.append(file)



    @staticmethod
    def get_files_from_cloud(user,current_preference):
        exist = []
        for root, directories, files in os.walk(Constants.cloud_folder_path(user, current_preference), topdown=True):
            for name in files:
                exist.append(os.path.join(root, name))
        return exist

    @staticmethod
    def check_cloud_folder_structure(current_user, curent_preference):
        if not os.path.exists(Constants.cloud_preference_folder_path(current_user)):
            os.mkdir(Constants.cloud_preference_folder_path(current_user))
        if not os.path.exists(Constants.cloud_folder_path(current_user, curent_preference)):
            os.mkdir(Constants.cloud_folder_path(current_user, curent_preference))
        if not os.path.exists(Constants.cloud_resource_folder_path(current_user, curent_preference)):
            os.mkdir(Constants.cloud_resource_folder_path(current_user, curent_preference))
        if not os.path.exists(Constants.cloud_module_folder_path(current_user, curent_preference)):
            os.mkdir(Constants.cloud_module_folder_path(current_user, curent_preference))
        if not os.path.exists(Constants.cloud_script_folder_path(current_user, curent_preference)):
            os.mkdir(Constants.cloud_script_folder_path(current_user, curent_preference))

    @staticmethod
    def check_preference():
        if not os.path.exists("Preference"):
            os.mkdir("Preference")
            for dir in Files.standart_dir():
                os.mkdir(f"Preference\\{dir}")
    @staticmethod
    def upload_file(current_user,curent_preference,filename,db):
        if File.query.filter_by(file_name=str(
                Constants.cloud_script_folder_path(current_user, curent_preference) + filename)).first() is None:
            file = File(
                file_name=str(Constants.cloud_script_folder_path(current_user, curent_preference) + filename))
            db.session.add(file)
            db.session.commit()
            preference_file = Preference_file(file_id=file.id, preference_id=curent_preference.preference_id)
            db.session.add(preference_file)
            db.session.commit()
    @staticmethod
    def run(cmd):
        os.environ['PYTHONUNBUFFERED'] = "1"
        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                )
        stdout, stderr = proc.communicate()

        return proc.returncode, stdout, stderr
