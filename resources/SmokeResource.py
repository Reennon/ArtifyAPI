from flask_restful import Resource
from ArtifyAPI.utils import socket_connect


class SmokeResorces(Resource):
    """
    GET endpoint hundler to test the process
    """

    def get(self):
        """
        send to core test message
        Returns (str): Test message "Hello"
        """
        socket_connect.socket_send("smoke")
        return 'Hello', 200

