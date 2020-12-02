import socket

from constants import Constants


class SocketConnection:

    @staticmethod
    def open_socket(host=Constants.LOCALHOST, port=Constants.PORT_CORE):
        """
        Args:
            host (string): host IP
            port (int): host port

        func open socket by host and port and returned socket client.

        Returns
             artify_socket (socket): connected client socked.
        """
        artify_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        artify_socket.connect((host, port))
        return artify_socket

    @staticmethod
    def socket_send(message):
        """
        Args:
            message (string): message by client

        func open socket in port 50000 and host '127.0.0.1'.

        encode and send message by socket to Core.

        at last close socket client.

        Returns
            None
        """

        artify_socket = SocketConnection.open_socket()
        artify_socket.sendall(message.encode())
        artify_socket.close()
