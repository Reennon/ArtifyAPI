from flask_restful import Resource
from utils.socket_connect import SocketConnection
from http import HTTPStatus


class BuildResource(Resource):
    """
    POST send Core command build project
    GET get from Core Build DLL from project
    """
    def get(self):
        """
        Get executable DLL from Core

        Returns:
             Http status OK
        """
        SocketConnection.socket_send(str({"command": "get_build"}))
        return HTTPStatus.OK

    def post(self):
        """
        send Core command build project

        Returns:
            Http response 200
        """

        SocketConnection.socket_send(str({"command": "build"}))
        return HTTPStatus.OK
