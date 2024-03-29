from flask_jwt_extended import jwt_required, get_jwt_identity

from flask_restful import Resource

from models.curent_preference import Curent_user_preference
from models.file import File
from models.preference_file import Preference_file
from models.preference_user import Preference_user
from models.user import User

class GetFolderTreeResource(Resource):
    @jwt_required()
    def get(self):
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()

        user_preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        curent_preference = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id,
                                                                   current_user_preference=True).first()
        user_preference_files = Preference_file.query.filter_by(preference_id=curent_preference.preference_id).all()
        paths = []
        for file in user_preference_files:
            paths.append((File.query.filter_by(id=file.file_id).first()).file_name)
        tree = {}
        for item in paths:
            currTree = tree
            item = item.split('\\')
            for key in item[::]:
                if key not in currTree:
                    currTree[key] = {}
                currTree = currTree[key]

        return tree
