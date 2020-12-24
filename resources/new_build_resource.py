from http import HTTPStatus

from flask import request
from flask_restful import Resource


class NewBuildResource(Resource):

    def post(self,id):
        data = request.get_data()
        path = str(data)
        print(f"for user with id {id}", str(path))
        return HTTPStatus.OK
