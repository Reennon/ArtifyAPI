from http import HTTPStatus

from flask import request
from flask_restful import Resource

from utils.socket_connect import SocketConnection


class UpdateExecutableResource(Resource):
    """
    POST update path to python executable
    """

    def post(self):
        """
        teke new python executble path and give iit to Core

        Returns:
             Http status Ok
        """
        data = request.get_json()
        enviroment = data["Environments"]
        modules = data["Modules"]
        update_exe = data["update_executable"]
        SocketConnection.socket_send(str({
            "command": "update_executable",
            "Environments": enviroment,
            "Nodules": modules,
            'update_executable': update_exe
        }))
        return HTTPStatus.OK
