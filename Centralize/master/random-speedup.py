#!/usr/bin/env python3
from scapy.all import *
import time
import random
import sys
import os

machine1 = "192.168.8.228"
machine2 = "192.168.169"
machine3 = "192.168.8.170"
machine4 = "192.168.8.155"
machine5 = "192.168.8.191"
machine0 = "192.168.8.255"

speed = float(sys.argv[1])
def sendPacket(machine):
    p1 = os.popen('echo "trigger" | nc -cu ' + machine + ' 10000')
    output = p1.read()

while True:
    random_Number = random.randint(1,6)
    
    if (speed < 20):
        if random_Number == 1:
            #send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="Trigger"))
            sendPacket(machine1)
        if random_Number == 2:
            sendPacket(machine2)
            #send(IP(dst="192.168.8.170")/UDP(dport=10000)/Raw(load="Trigger"))
        if random_Number == 3:
            sendPacket(machine3)
           #send(IP(dst="192.168.8.169")/UDP(dport=10000)/Raw(load="Trigger!"))
        if random_Number == 4:
            sendPacket(machine4)
            
           #send(IP(dst="192.168.8.155")/UDP(dport=10000)/Raw(load="servo;\n"))
        if random_Number == 5:
            sendPacket(machine5)
#           send(IP(dst="192.168.8.191")/UDP(dport=10000)/Raw(load="Trigger tin"))
        if random_Number == 6:
            sendPacket(machine1)
            sendPacket(machine2)
            sendPacket(machine3)
            sendPacket(machine4)
            sendPacket(machine5)
           #send(IP(dst="192.168.8.255")/UDP(dport=10000)/Raw(load="servo;\n"))
    else:
        break
    time.sleep(random.random()/speed)
    speed = speed + 0.1
