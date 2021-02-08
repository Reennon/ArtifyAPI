from flask import request
from werkzeug.security import generate_password_hash

from app import db
from auth.auth import auth
from models.curent_preference import Curent_user_preference
from models.preference import Preference
from models.preference_user import Preference_user
from models.user import User


@auth.route('/artify/signup', methods=['POST'])
def signup():
    """ POST method
            request for creating user on DataBase

    Args:
        request body (json):
                            {
                                "username":"soft",      // User name
                                "password":"soft",      // User password
                                "email":"Artify@Artify.com"     // User E-mail
                            }
    Returns:
        string: <hello {username}>
        response OK 200
    """

    data = request.get_json()
    name = data['username']
    password = data['password']
    email = data['email']

    user = User.query.filter_by(email=email).first()
    if user:
        return "this user already registered"

    new_user = User(username=name, password=generate_password_hash(password, method='sha256'), email=email)
    db.session.add(new_user)
    db.session.commit()
    new_preference = Preference()
    db.session.add(new_preference)
    db.session.commit()
    new_user_preference = Preference_user(preference_id=new_preference.id, user_id=new_user.id)
    db.session.add(new_user_preference)
    db.session.commit()
    new_current_preference = Curent_user_preference(preference_id=new_preference.id,
                                                    preference_user_id=new_user_preference.id,
                                                    current_user_preference=True,
                                                    name=f"Preference_{new_user.username}")

    db.session.add(new_current_preference)
    db.session.commit()

    return f"hello {new_user.username}"
