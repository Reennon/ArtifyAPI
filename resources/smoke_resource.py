from http import HTTPStatus

from flask_login import login_required, current_user
from flask_restful import Resource

from models.curent_preference import Curent_user_preference
from models.preference_user import Preference_user
from utils.files import Files

class SmokeResorces(Resource):
    """
    GET endpoint handler to test the process
    """

    @login_required
    def get(self):
        """
        send to core test message
        Returns (str): Test message "Hello"
        """
        """user_preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        current_preference = Curent_user_preference.query.filter_by(current_user_preference=True,
                                                                preference_user_id=user_preference_user.id).first()
        Files.update_db(current_user,current_preference)"""
        return f'{current_user.username}', HTTPStatus.OK
