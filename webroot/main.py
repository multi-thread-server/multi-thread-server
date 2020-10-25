#!/usr/bin/python3

import threading
from server import Server
from cgi import *   # import all cgi apps

def main():
    server = Server('127.0.0.1', 8888).start()

if __name__ == '__main__':
    main()
