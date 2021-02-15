from http import HTTPStatus

from flask_restful import Resource


from flask import flash
from flask import request

from werkzeug.security import check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from app import db
from auth.auth import auth
from models.user import User
from utils.files import Files


class LoginResource(Resource):

    def post(self):
        """
        POST method

        Point:
            Logging in user and manage his folders on cloud to local

        Args:
            request body (json):
                                {
                                    "preference_name":"Artify",
                                    "password":"s",
                                    "email":"s@s.com"
                                }

        Returns:
            string: <hello {username}, welcome on {preference_name}>
            response OK 200

        """

        data = request.get_json()
        password = data['password']
        email = data['email']
        preference_name = data['preference_name']
        Files.check_preference()


        user = User.query.filter_by(email=email).first()

        if not user and not check_password_hash(user.password, password):
            flash("wrong password or email ")
            return HTTPStatus.BAD_REQUEST
        if user.email != 'user':
            Files.prepear_to_logout()

        token = Files.prepear_to_login(user, preference_name, db)

        return token
