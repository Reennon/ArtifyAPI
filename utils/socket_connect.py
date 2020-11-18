import socket


def open_socket(host='127.0.0.1', port=50000):
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

    artify_socket = open_socket()
    artify_socket.sendall(message.encode())
    artify_socket.close()

