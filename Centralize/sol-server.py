#!/usr/bin/env python3
import socket
import sys
from TriggerSolenoid import *
from Indicator import *
from ServoMotor import *
from signal import signal, SIGINT
from sys import exit

def handler(signal_received, frame):
    # Handle any cleanup here
    print('Server shutting down... Goodbye.')
    exit(0)

sol = Solenoid(4)
indicator = Indicator('red')
#servo = ServoMotor(21, "low")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
local_hostname = socket.gethostname()
print("This is \033[1;31;40m" + local_hostname + "\033[39m.")
ip_address = socket.gethostbyname(local_hostname)
#print(ip_address)
#server_address = ('192.168.8.145', 10000)
server_address = ('', 10000)
print('Starting server on%s port %s' % server_address)
sock.bind(server_address)

if __name__ == '__main__':
    signal(SIGINT, handler)

    while True:
        print('\nwaiting to receive message')
        data, address = sock.recvfrom(4096)
        remoteHost =  socket.gethostbyaddr(address[0])
        #print('received %s bytes from %s' % (len(data), address))
        print('\nreceived %s from %s' % (data.decode("utf-8"), remoteHost[0]))

        if data:
            #print("data recvd")
            sent = sock.sendto(data, address)
#            print('sent %s bytes back to %s' % (sent, address))

            if data == b"servo;\n":
                swipe()
            else:
                indicator.fadeIn()
                sol.trigger()
           #     print("solenoid triggered")

