from http import HTTPStatus

from flask_restful import Resource
from flask import request
from utils.socket_connect import SocketConnection


class ErrorResource(Resource):


    def post(self,id):
        """ POST method send error log from Core to Api

        Args:
            id (int):  User id from DataBase

        Returns:
            Http response OK 200
        """
        data = request.get_data()
        print(f"for user with id {id}", str(data))
        return HTTPStatus.OK
