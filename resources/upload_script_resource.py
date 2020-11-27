from flask_restful import Resource
from constants import Constants
from flask import request, flash
from utils.utils import Utils
from utils.socket_connect import SocketConnection
from http import HTTPStatus
import os


class UploadScriptResource(Resource):
    """
    POST endpoint handler to save script photo by user
    GET endpoint handler run script on Core
    """

    def get(self):
        """
        run script from folder S/Script on core

        Returns:
             Http response OK
        """
        SocketConnection.socket_send(str({"command": "run script"}))
        return HTTPStatus.OK

    def post(self):
        """
        Args:
            file from request (flask.request.files['file']): script which send user

        func set file by request and save it on server in folder 'data-storage/Script/' and
        send Core message with name of script.

        Returns:
            200 OK
        """
        file = request.files['file']
        if not file.filename:
            return flash("None selected script")
        if not Utils.allowed_script_type(filename=file.filename):
            return flash("this image not allowed")
        file.save(os.path.join(Constants.SCRIPT_FOLDER_PATH, file.filename))

        return HTTPStatus.OK



