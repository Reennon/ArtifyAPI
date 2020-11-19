from flask_restful import Resource
from ArtifyAPI.utils.socket_connect import SocketConnection
from http import HTTPStatus

class SmokeResorces(Resource):
    """
    GET endpoint hundler to test the process
    """

    def get(self):
        """
        send to core test message
        Returns (str): Test message "Hello"
        """
        SocketConnection.socket_send("smoke")
        return 'Hello', HTTPStatus.OK

