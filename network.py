__author__ = "Trang Ha"

import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.123"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        self.client.connect(self.addr)
        return pickle.loads(self.client.recv(2048))

    def send(self, data):
        self.client.send(pickle.dumps(data))
        return pickle.loads(self.client.recv(2048))
