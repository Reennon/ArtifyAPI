from auth.auth import auth
from flask import request
from flask import flash
from models.user import User
from werkzeug.security import check_password_hash
from http import HTTPStatus
from flask_login import login_user, logout_user,login_required,current_user


@auth.route('/logout')
@login_required
def logout():
    if current_user.username == 'user':
        return "you are a standard user"
    name = current_user.username
    logout_user()

    return f"goodbye {name}"
