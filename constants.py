
class Constants:
    """
    Allowed Extensions
    """
    ALLOWED_EXTENSIONS_FOR_PHOTO = {'png', 'jpg', 'jpeg'}
    ALLOWED_EXTENSIONS_FOR_SCRIPT = {'cs', 'py', 'dll'}

    """
    Allowed folder path
    """
    PHOTO_FOLDER_PATH = r'data-storage/Photo'
    SCRIPT_FOLDER_PATH = 'Preference\\Scripts\\'
    MODULE_FOLDER_PATH = 'Preference\\Modules\\'
    CLOUD_SCRIPT_FOLDER_PATH = 'Cloud\\Scripts\\'
    CLOUD_MODULE_FOLDER_PATH = 'Cloud\\Modules\\'
    @staticmethod
    def cloud_module_folder_path(user, preference):
        return "Cloud\\Preference_user_"+str(user.id)+"\\"+str(preference.name)+"\\Modules\\"

    @staticmethod
    def cloud_script_folder_path(user, preference):
        return "Cloud\\Preference_user_" + str(user.id) + "\\" + str(preference.name) + "\\Scripts\\"
    """
    Hosts
    """
    LOCALHOST = '127.0.0.1'

    """
    Ports
    """
    PORT_CORE = 50000
