from flask_login import logout_user, login_required, current_user

from auth.auth import auth
from utils.files import Files

@auth.route('/logout')
@login_required
def logout():
    """
    GET method

    Logout user from API and DELETE all files from locals folder

    Returns:
        response OK 200
    """
    if current_user.username == 'user':
        return "you are a standard user"
    name = current_user.username
    Files.prepear_to_logout()
    logout_user()

    return f"goodbye {name}"
