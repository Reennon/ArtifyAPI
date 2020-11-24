from flask_restful import Resource
from utils.socket_connect import SocketConnection
from http import HTTPStatus

class SmokeResorces(Resource):
    """
    GET endpoint handler to test the process
    """

    def get(self):
        """
        send to core test message
        Returns (str): Test message "Hello"
        """
        SocketConnection.socket_send("smoke")
        return 'Hello', HTTPStatus.OK

