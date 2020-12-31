from http import HTTPStatus

from flask import flash
from flask import request
from flask_login import current_user, logout_user
from werkzeug.security import check_password_hash

from app import db
from auth.auth import auth
from models.user import User
from utils.files import Files


@auth.route('/login', methods=['POST'])
def login():
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
    if current_user.email is user.email:
        return "you already logged in "
    if user.email != 'user':
        Files.prepear_to_logout()
        logout_user()

    Files.prepear_to_login(user, preference_name, db)

    return f"hello {user.username}, welcome on {preference_name}"
