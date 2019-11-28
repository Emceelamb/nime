#!/usr/bin/env python3
from scapy.all import *
import time
import random
import os

woodblock = "192.168.8.228"
coffeetin = "192.168.8.191"
goldtin = "192.168.8.170"
woodspring = "192.168.8.169"
servospring = "192.168.8.155"

def sendPackets(c=1, i=0):
    s.send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="Trigger"), realtime=1, count=c, inter=i)

def sendPacket(soundobject):
    if soundobject == servospring:
        p1 = os.popen('echo "servo;\n" | nc -cu '+ soundobject + ' 10000')
        output = p1.read()

    else:
        p1 = os.popen('echo "hi" | nc -cu '+ soundobject + ' 10000')
        output = p1.read()


def buildup():
    running = True
    timeout = 10

    while running:
        sendPacket(servospring)
        time.sleep(timeout)
        timeout = timeout - 1
        if(timeout < 1):
            for x in range (1, 5):
                sendPacket(servospring)
                time.sleep(1)
            running = False


buildup()
