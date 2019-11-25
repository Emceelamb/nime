#!/usr/bin/env python3
import socket
import sys
from TriggerSolenoid import *
from Indicator import *
from ServoMotor import *
from signal import signal, SIGINT
from sys import exit
from colorama import Fore, Style

def handler(signal_received, frame):
    # Handle any cleanup here
    print(Fore.GREEN+'Server shutting down... Goodbye.'+Style.RESET_ALL)
    exit(0)

sol = Solenoid(4)
indicator = Indicator('red')
#servo = ServoMotor(21, "low")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
local_hostname = socket.gethostname()
print("This is " + Fore.RED +  local_hostname + Style.RESET_ALL+".")
ip_address = socket.gethostbyname(local_hostname)
#print(ip_address)
#server_address = ('192.168.8.145', 10000)
server_address = ('', 10000)
print('Starting server on%s port %s' % server_address)
sock.bind(server_address)

# lookup remote host
def lookup(addr):
    try:
        return str(socket.gethostbyaddr(addr))
    except socket.herror:
        return str(addr)

if __name__ == '__main__':
    signal(SIGINT, handler)

    while True:
        print(Fore.YELLOW+'\nwaiting to receive message'+Style.RESET_ALL)
        data, address = sock.recvfrom(4096)
        #remoteHost =  socket.gethostbyaddr()
        remoteHost =  lookup(address[0])
        print('\nreceived ' + '%s from ' % data.decode("utf-8") + Fore.RED+'%s'  % remoteHost)
        #print('\nreceived ' + '%s from ' % data.decode("utf-8") + Fore.RED+'%s'  % str(address[0]))

        if data:
            sent = sock.sendto(data, address)
#            print('sent %s bytes back to %s' % (sent, address))

            if data == b"servo;\n":
                swipe()
            else:
                indicator.fadeIn()
                sol.trigger()

