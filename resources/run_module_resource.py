import os
from http import HTTPStatus

from flask import request, flash
from flask_restful import Resource

from constants import Constants
from utils.socket_connect import SocketConnection
from utils.utils import Utils


class ModuleResource(Resource):
    """
    POST Upload user modules
    GET Run user modules
    """

    def get(self):
        """
        send core select module

        """
        data = request.get_json()
        if data is None:
            return HTTPStatus.BAD_REQUEST
        SocketConnection.socket_send(str(data))
        return HTTPStatus.OK

    def post(self):
        """
            Args:
                file from request (flask.request.files['file']): module which send user

                func set file by request and save it on server in folder 'data-storage/Module/' and
                send Core message with name of Module.

            Returns:
                200 OK
        """
        file = request.files['file']
        if not file.filename:
            return flash("None selected script")
        if not Utils.allowed_script_type(filename=file.filename):
            return flash("this image not allowed")
        file.save(os.path.join(Constants.MODULE_FOLDER_PATH, file.filename))

        return HTTPStatus.OK
