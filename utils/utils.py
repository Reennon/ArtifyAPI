import os
import shutil
import zipfile

from constants import Constants


class Utils:
    @staticmethod
    def allowed_photo_type(filename):
        """
        Args:
            filename (string): photo name

        func check if photo file name extensions is correct.

        Returns:
            (bool): if file Ok it be True, in else False
        """

        if '.' in filename:
            extension = filename.rsplit('.', 1)[1].lower()
            return extension in Constants.ALLOWED_EXTENSIONS_FOR_PHOTO
        else:
            return False

    @staticmethod
    def allowed_script_type(filename):
        """
        Args:
            filename (string): photo name

        func check if script file name extensions is correct.

        Returns:
            (bool): if file Ok it be True, in else False
        """

        if '.' in filename:
            extension = filename.rsplit('.', 1)[1].lower()
            return extension in Constants.ALLOWED_EXTENSIONS_FOR_SCRIPT
        else:
            return False

    @staticmethod
    def unzip_folder(path, name):
        zip = zipfile.ZipFile(path)
        os.mkdir(name)
        zip.extractall(path=name)

    @staticmethod
    def check_cloud_folder_structure(current_user, curent_preference):
        if not os.path.exists(Constants.cloud_preference_folder_path(current_user)):
            os.mkdir(Constants.cloud_preference_folder_path(current_user))
        if not os.path.exists(Constants.cloud_folder_path(current_user,curent_preference)):
            os.mkdir(Constants.cloud_folder_path(current_user,curent_preference))
        if not os.path.exists(Constants.cloud_resource_folder_path(current_user, curent_preference)):
            os.mkdir(Constants.cloud_resource_folder_path(current_user, curent_preference))
        if not os.path.exists(Constants.cloud_module_folder_path(current_user, curent_preference)):
            os.mkdir(Constants.cloud_module_folder_path(current_user, curent_preference))
        if not os.path.exists(Constants.cloud_script_folder_path(current_user, curent_preference)):
            os.mkdir(Constants.cloud_script_folder_path(current_user, curent_preference))
