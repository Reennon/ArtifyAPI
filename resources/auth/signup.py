from flask import request
from werkzeug.security import generate_password_hash

from app import db
from auth.auth import auth
from models.user import User


@auth.route('/signup', methods={'POST'})
def signup():
    data = request.get_json()
    name = data['username']
    password = data['password']
    email = data['email']

    user = User.query.filter_by(email=email).first()
    if user:
        return "this user already registered"

    new_user = User( username=name, password=generate_password_hash(password, method='sha256'), email=email)
    db.session.add(new_user)
    db.session.commit()
    return f"hello {new_user.username}"
