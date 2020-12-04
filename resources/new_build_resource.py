from http import HTTPStatus

from flask import request
from flask_restful import Resource

from utils.socket_connect import SocketConnection


class NewBuildResource(Resource):

    def post(self):
        data = request.get_json()
        path = data["path"]
        print(path)
        return HTTPStatus.OK
