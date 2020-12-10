from http import HTTPStatus

from flask import flash
from flask import request
from flask_login import login_user
from werkzeug.security import check_password_hash

from auth.auth import auth
from models.user import User


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    password = data['password']
    email = data['email']

    user = User.query.filter_by(email=email).first()
    if not user and not check_password_hash(user.password, password):
        flash("wrong password or email ")
        return HTTPStatus.BAD_REQUEST

    login_user(user)

    return f"hello {user.username}"
