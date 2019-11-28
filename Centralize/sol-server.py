#!/usr/bin/env python3
import socket
import sys
from TriggerSolenoid import *
from Indicator import *
from ServoMotor import *
from signal import signal, SIGINT
from sys import exit
from colorama import Fore, Style
import time
import threading
import gpiozero


# Set solenoid pins
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
        return socket.gethostbyaddr(addr)
    except socket.herror:
        return addr

# Goodbye message

def handler(signal_received, frame):
    # Handle any cleanup here
    print(Fore.GREEN+'Server shutting down... Goodbye.'+Style.RESET_ALL)
    exit(0)

# LEDs
RELAY_PIN = 26
relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)
relay_state = 0

"""
def toggle_relay():
    relay.on()
    if(timer.is_alive() is True):
        timer.cancel()
        relay.off()
    else: 
        timer.start()

timer = threading.Timer(1.0, toggle_relay)
"""

def toggle_relay():
    global relay_state
    if (relay_state == 0):
        relay.on()
        relay_state = 1
    else:
        relay.off()
        relay_state = 0



def startupSeq():
    relay.on()
    sol.trigger()
    time.sleep(1)
    sol.trigger()
    time.sleep(1)
    sol.trigger()
    time.sleep(1)
    relay.off()


if __name__ == '__main__':
    signal(SIGINT, handler)

    startupSeq()

    while True:
        print(Fore.YELLOW+'\nwaiting to receive message'+Style.RESET_ALL)
        data, address = sock.recvfrom(4096)
        #remoteHost =  socket.gethostbyaddr()
        remoteHost =  lookup(address[0])
        print('\nreceived ' + '%s from ' % data.decode("utf-8") + Fore.RED+'%s'  % str(remoteHost[0]))
        #print('\nreceived ' + '%s from ' % data.decode("utf-8") + Fore.RED+'%s'  % str(address[0]))

        if data:
            toggle_relay()

            if data == b"servo;\n":
                swipe()
            else:
                indicator.fadeIn()
                sol.trigger()
