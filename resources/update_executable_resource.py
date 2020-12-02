from flask_restful import Resource
from flask import request
from utils.socket_connect import SocketConnection
from http import HTTPStatus


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
        SocketConnection.socket_send(str(data))
        return HTTPStatus.OK