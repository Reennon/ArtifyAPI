from flask_jwt_extended import jwt_required, get_jwt_identity

from flask_restful import Resource

from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from models.user import User

class GetUserProjectResource(Resource):
    @jwt_required()
    def get(self):
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()
        if current_user.username == "user":
            return {
                "user_projects": [
                    "Standart"
                ]
            }
        user_preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        all_curent_preference = Curent_user_preference.query.filter_by(preference_user_id=user_preference_user.id).all()
        user_projects = []
        for pref in all_curent_preference:
            user_projects.append(pref.name)
        json = {"user_projects": user_projects}
        return json
