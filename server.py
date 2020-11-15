__author__ = "Trang Ha"

import socket
from _thread import *
from main import Player
import pickle
import random

server = "192.168.1.123"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)
print("Waiting for a connection, Server Started")

# Set up random pictionary word
with open("pictionary.txt", "r") as pictionary:
    w = pictionary.read().split()

def newWord():
    return random.choice(w)

randomWord = newWord()
print(randomWord)

players = [Player(800, 600, 1, randomWord), Player(800, 600, 2, randomWord)]

def threaded_client(conn, playerID):
    conn.send(pickle.dumps(players[playerID]))
    while True:
        data = pickle.loads(conn.recv(2048))
        players[playerID] = data

        if not data:
            print("Disconnected")
            break
        else:
            if playerID == 1:
                reply = players[0]
            else:
                reply = players[1]

            print("Received: ", data)
            print("Sending : ", reply)

        conn.sendall(pickle.dumps(reply))

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1


