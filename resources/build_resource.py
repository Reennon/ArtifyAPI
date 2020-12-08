from http import HTTPStatus

from flask import request
from flask_restful import Resource

from utils.socket_connect import SocketConnection


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
        data = request.get_json()
        dllName = data['dllName']

        SocketConnection.socket_send(str(
            {
                "command": "build",
                "dllName": "dllName" if dllName is None else dllName
            }))
        return HTTPStatus.OK
