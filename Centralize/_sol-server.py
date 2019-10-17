#!/usr/bin/env python3
import socket
import sys
from TriggerSolenoid import *
#from Indicator import *
from ServoMotor import *
from gpiozero import RGBLED

sol = Solenoid(4)
#indicator = Indicator('red')
indicator = RGBLED(red=22, green=9, blue=10)
#servo = ServoMotor(21, "low")

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

# LED light
indicator_state = True
start_sec = int(time.time())
previous_sec = start_sec

def indicator_on():
    global indicator_state
    indicator_state = False

def indicator_off():
    global indicator_state
    indicator_state = False
i = 0
while True:
    elapsed_time = int(time.time()) - start_sec
    print(indicator_state)

    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received %s bytes from %s' % (len(data), address))
    print(data)

    if data:
        print("data recvd")
        sent = sock.sendto(data, address)
        print('sent %s bytes back to %s' % (sent, address))
        
        packet_received_time = int(time.time())
        

        if data == b"servo;\n":
            swipe()
            print("Servod")
        else:
            #indicator.fadeIn()
            sol.trigger()
            print("solenoid triggered")

    print(indicator_state)
    if indicator_state == False and int(time.time()) - packet_received_time > 0.5:
        indicator_state = True
        time.sleep(0.1)
        indicator_state = False

    if indicator_state:
        indicator.on()
    else:
        indicator.off()

