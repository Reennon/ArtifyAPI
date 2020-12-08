from flask_restful import Resource
from utils.socket_connect import SocketConnection
from flask_login import login_required,current_user
from http import HTTPStatus

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

        return f'{current_user.username}', HTTPStatus.OK

