#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket,threading

HOST = '0.0.0.0'
PORT = 7000
list_of_clients=[]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')
def clientthread(conn, addr):

    # sends a message to the client whose user object is conn
    conn.send("Welcome to this chatroom!".encode("utf-8"))

    while True:
        try:
            message = conn.recv(2048)
            if len(message) != 0:
                print("<" + addr[0] + "> " + message.decode("utf-8"))

                # Calls broadcast function to send message to all
                message_to_send = "<" + addr[0] + "> " + message.decode("utf-8")
                broadcast(message_to_send, conn)

            else:
                print('server closed connection.')
                remove(conn)

        except:
            continue

while True:
    conn, addr = s.accept()

    list_of_clients.append(conn)

    print(addr[0] + " connected")

    threading.Thread(target = clientthread, args = (conn, addr))

conn.close()
server.close()