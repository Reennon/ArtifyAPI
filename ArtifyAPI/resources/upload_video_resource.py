from flask_restful import Resource
from ArtifyAPI.constants import Constants
from flask import request, flash
from ArtifyAPI.utils.utils import Utils
from ArtifyAPI.utils.socket_connect import SocketConnection
from http import HTTPStatus
import os


class UploadVideoResource(Resource):
    """
    POST endpoint handler to save upload photo by user
    """

    def post(self):
        """
        Args:
            file from request (flask.request.files['file']): video which send user

        func set file by request and save it on server in folder 'Video/' and
        send Core message with name of video.

        Returns:
            200 OK
        """
        file = request.files['file']
        if not file.filename:
            return flash("None selected video")
        if not Utils.allowed_video_type(filename=file.filename):
            return flash("this video not allowed")
        file.save(os.path.join(Constants.VIDEO_FOLDER_PATH, file.filename))
        SocketConnection.socket_send(str({"message": ('video/' + file.filename)}))

        return HTTPStatus.OK


