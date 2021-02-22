from http import HTTPStatus

from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from flask_restful import Resource

from constants import Constants
from models.preference_user import Preference_user
from utils.socket_connect import SocketConnection
from models.curent_preference import Curent_user_preference
from models.user import User

class BuildResource(Resource):
    """
    POST send Core command build project
    GET get from Core Build DLL from project
    """

    def get(self):
        """
        Get executable DLL from Core

        Returns:
             Http status OK
        """
        SocketConnection.socket_send(str({"command": "get_build"}))
        return HTTPStatus.OK

    @jwt_required()
    def post(self):
        """
        Point:
            send Core command build project

        Args:
            JSON string

        JSON STRUCTURE
             KEY                TYPE        DESC
        {
            "command": "build"  #string     build command tells core which command to execute
            , "userId":         #int        User ID is required for core to return the build, user gave
            , "dllName":        #string     Dll Name is required for core to name the build, user specified
            , "path":           #string     Path to the preference folder on cloud
            , "ASSEMBLY_NAME":  #string     Assembly Name is not required for core, but preferred to have one,
                                #           otherwise core will name it by itself
            , "UNSAFE_CODE":    #boolean    Unsafe Code
            , "NECESSARY_DLLS": #string[]   Necessary Dlls is not required for core, if empty, default libs will
                                #           be linked in memory and end-product dll. Below listed default libs,
                                #           that are required for compiled program to be executed
                                #           "System.Private.CoreLib", "System.Console", "System.Runtime", "mscorlib"
        }

        Returns:
            Http response 200

        """
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()
        preference_user = Preference_user.query.filter_by(user_id=current_user.id).first()
        current_preference = Curent_user_preference(preference_user_id=preference_user.id, current_user_preference=True)
        data = request.get_json()
        user_id = data["userId"]
        dll_name = data.get("dllName", "application")
        path = Constants.cloud_folder_path(current_user, current_preference)
        assembly_name = data.get("ASSEMBLY_NAME", None)
        unsafe_code = data.get("UNSAFE_CODE", False)
        necessary_dlls = data.get("NECESSARY_DLLS", None)

        import json
        SocketConnection.socket_send(json.dumps(
            {
                "command": "build"
                , "userId": user_id
                , "dllName": dll_name
                , "path": path
                , "ASSEMBLY_NAME": assembly_name
                , "UNSAFE_CODE": unsafe_code
                , "NECESSARY_DLLS": necessary_dlls

            }))
        return HTTPStatus.OK
