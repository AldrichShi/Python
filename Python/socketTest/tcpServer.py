# -*- coding: utf-8 -*-
# tcpServer.py
# @author King
# @description
# @created 2019-06-26T18:03:38.295Z+08:00
# @last-modified 2019-06-26T18:26:16.784Z+08:00
#

import socket
from time import ctime
HOST = ""
PORT = '21567'
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind((socket.gethostname(), 21567))
tcpSerSock.listen(5)
while True:
    print('waiting for connection .....')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connect from:', addr)
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s]%s', bytes(ctime(), 'utf-8'), data)
        tcpCliSock.close
tcpSerSock.close
