from flask_login import logout_user, login_required, current_user

from auth.auth import auth


@auth.route('/logout')
@login_required
def logout():
    if current_user.username == 'user':
        return "you are a standard user"
    name = current_user.username
    logout_user()

    return f"goodbye {name}"
