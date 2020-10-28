import socket
import threading
import logging
from http import HttpRequest, HttpResponse
from cgi_bin.cgi import cgi
from cgi_bin import calculator   # import all cgi apps
from log import log

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
        log('{} - {} - {} - {}'.format(self.address, 
            http_request.get_method(), http_request.get_url(), 
            http_response.get_content_type()))
        self.client_socket.close()

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
            session = Session(client_socket, address)
            threading.Thread(target=session.run).start()
