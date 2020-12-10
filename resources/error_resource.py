from http import HTTPStatus

from flask_restful import Resource
from flask import request
from utils.socket_connect import SocketConnection


class ErrorResource(Resource):


    def post(self,id):
        data = request.get_data()
        print(f"for user with id {id}", str(data))
        return HTTPStatus.OK
