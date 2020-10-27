import socket
import threading
from http import HttpRequest, HttpResponse
from cgi_bin.cgi import cgi
from cgi_bin import calculator   # import all cgi apps

class Session:

    def __init__(self, client_socket, address):
        # TODO: remove address
        self.client_socket, self.address = client_socket, address

    def run(self):
        http_request = HttpRequest()
        while not http_request.is_parse_completed:
            data = self.client_socket.recv(1024)
            http_request.feed_data(data)
        http_response = cgi(http_request)
        self.client_socket.send(http_response.build_http())
        self.client_socket.close()
        print('session closed')

class Server:

    def __init__(self, host, port):
        self.host, self.port = host, port

    def start(self):
        self.server_socket = socket.socket()
        self.server_socket.bind((self.host, self.port))
        # TODO: listen num
        self.server_socket.listen(1)

        while True:
            client_socket, address = self.server_socket.accept()
            # TODO: write log
            print('socket established with {}.'.format(address))
            session = Session(client_socket, address)
            threading.Thread(target=session.run).start()
