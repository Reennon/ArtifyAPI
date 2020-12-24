from http import HTTPStatus

from flask_restful import Resource

from utils.socket_connect import SocketConnection


class RunBuildResource(Resource):
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

        SocketConnection.socket_send(str({"command": "run_build"}))

        return HTTPStatus.OK
