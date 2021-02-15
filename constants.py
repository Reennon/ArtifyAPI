
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
    PREFERENCE_PATH = 'Preference\\'
    RESOURCE_FOLDER_PATH = 'Preference\\Resources\\'
    CLOUD_SCRIPT_FOLDER_PATH = 'Cloud\\Scripts\\'
    CLOUD_MODULE_FOLDER_PATH = 'Cloud\\Modules\\'
    CLOUD_PATH = 'Cloud'
    CORS_ORIGINS = r"http://localhost:5000", r"https://localhost:5001", r"http://192.168.0.104:5000"

    @staticmethod
    def cloud_module_folder_path(user, preference):
        return "Cloud\\Preference_user_"+str(user.id)+"\\"+str(preference.name)+"\\Modules\\"

    @staticmethod
    def cloud_script_folder_path(user, preference):
        return "Cloud\\Preference_user_" + str(user.id) + "\\" + str(preference.name) + "\\Scripts\\"

    @staticmethod
    def cloud_resource_folder_path(user, preference):
        return "Cloud\\Preference_user_" + str(user.id) + "\\" + str(preference.name) + "\\Resources\\"

    @staticmethod
    def cloud_folder_path(user, preference):
        return "Cloud\\Preference_user_" + str(user.id) + "\\" + str(preference.name) + "\\"

    @staticmethod
    def cloud_preference_folder_path(user):
        return "Cloud\\Preference_user_" + str(user.id) + "\\"


    """
    Hosts
    """
    LOCALHOST = '127.0.0.1'
    HOST = '192.168.0.103'

    """
    Ports
    """
    PORT_CORE = 50000

    """
    DATABASE
    """
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1@localhost:5432/artify_db"
    SECRET_KEY = 'stepan'