from http import HTTPStatus

from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from models.user import User


class SmokeResorces(Resource):
    """
    GET endpoint handler to test the process
    """

    @jwt_required()
    def get(self):
        """
        send to core test message
        Returns (str): Test message "Hello"
        """
        """user_preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        current_preference = Curent_user_preference.query.filter_by(current_user_preference=True,
                                                                preference_user_id=user_preference_user.id).first()
        Files.update_db(current_user,current_preference)"""
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()
        return f'{current_user.username}', HTTPStatus.OK
