#!/usr/bin/env python3
import socket
import sys
from TriggerSolenoid import *
from Indicator import *

sol = Solenoid(4)
indicator = Indicator('red')

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
local_hostname = socket.gethostname()
print(local_hostname)
ip_address = socket.gethostbyname(local_hostname)
print(ip_address)
#server_address = ('192.168.8.145', 10000)
server_address = ('', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received %s bytes from %s' % (len(data), address))
    print(data)

    if data:
        print("data recvd")
        sent = sock.sendto(data, address)
        print('sent %s bytes back to %s' % (sent, address))
        print("solenoid triggered")

        indicator.fadeIn()
        sol.trigger()
