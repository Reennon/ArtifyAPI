from flask_restful import Resource
from ArtifyAPI.utils import utils
from ArtifyAPI import constants
from flask import request, flash
from ArtifyAPI.utils import socket_connect
import os


class UploadPhotoResource(Resource):
    """
    POST endpoint hundler to save upload photo by user
    """

    def post(self):
        """
        Args:
            file from request (flask.request.files['file']): photo which send user

        func set file by request and save it on server in folder 'Photo/' and
        send Core message with name of photo.

        Returns:
            200
        """
        file = request.files['file']
        if file.filename == '':
            return flash("None selected photo")
        if not utils.allowed_photo_type(filename=file.filename):
            return flash("this image not allowed")
        file.save(os.path.join(constants.PHOTO_FOLDER_PATH, file.filename))
        message = 'photo/' + file.filename
        mes = {"message": message}
        socket_connect.socket_send(str(mes))

        return 200



