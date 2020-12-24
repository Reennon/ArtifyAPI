from http import HTTPStatus
from flask import request
from flask_restful import Resource


class NewBuildResource(Resource):

    def post(self, id):
        """POST request which handle Core release folder path

        Args:
            id (int):  User id from DataBase
            request body (string): path tothe Relase folder

        Returns:
            Http response 200

        """
        data = request.get_data()
        path = str(data)
        print(f"for user with id {id}", str(path))
        return HTTPStatus.OK
