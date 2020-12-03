from flask_restful import Resource
from constants import Constants
from flask import request, flash
from utils.utils import Utils
from utils.socket_connect import SocketConnection
from http import HTTPStatus
import os


class UploadPhotoResource(Resource):
    """
    POST endpoint handler to save upload photo by user
    """

    def post(self):
        """
        Args:
            file from request (flask.request.files['file']): photo which send user

        func set file by request and save it on server in folder 'data-storage/Photo/' and
        send Core message with name of photo.

        Returns:
            200 OK
        """
        file = request.files['file']
        if not file.filename:
            return flash("None selected photo")
        if not Utils.allowed_photo_type(filename=file.filename):
            return flash("this image not allowed")
        file.save(os.path.join(Constants.PHOTO_FOLDER_PATH, file.filename))
        SocketConnection.socket_send(str({"message": (Constants.PHOTO_FOLDER_PATH + file.filename)}))

        return HTTPStatus.OK



