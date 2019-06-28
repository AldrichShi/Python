# -*- coding: utf-8 -*-
# socket.py
# @author King
# @description
# @created 2019-06-26T17:23:59.502Z+08:00
# @last-modified 2019-06-26T22:42:09.144Z+08:00
#

import socket

HOST = '127.0.0.1'  # or 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect((socket.gethostname(), 21567))
while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.sendall(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data)
tcpCliSock.close
