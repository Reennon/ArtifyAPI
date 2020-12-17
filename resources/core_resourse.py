from http import HTTPStatus
from flask_restful import Resource
from utils.socket_connect import SocketConnection
from subprocess import Popen, CREATE_NEW_CONSOLE
import threading


class CoreStartResource(Resource):
    """
    GET endpoint handler to test the process
    """

    def post(self):
        """
        send to core message to start
        Returns (str): Test message "Success!"
        """
        th1 = threading.Thread(target=t1)
        th1.start()
        SocketConnection.socket_send("core_start")
        return HTTPStatus.OK


def t1():
    Popen('C:/Windows/System32/notepad.exe', creationflags=CREATE_NEW_CONSOLE)
