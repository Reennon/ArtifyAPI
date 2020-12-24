from flask_login import logout_user, login_required, current_user
import os
from auth.auth import auth


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
    module_location = "...\\..\\Preference\\Modules\\"
    script_location = "...\\..\\Preference\\Scripts\\"
    moddules = os.listdir(os.path.abspath("...\\..\\Preference\\Modules"))
    scripts = os.listdir(os.path.abspath("...\\..\\Preference\\Scripts"))
    for script in scripts:
        print("DELETE",script_location+script)
        os.remove(script_location+script)

    for module in moddules:
        print("DELETE", module_location + module)
        os.remove( module_location + module)
    logout_user()

    return f"goodbye {name}"
