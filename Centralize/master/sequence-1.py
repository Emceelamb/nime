#!/usr/bin/env python3
from scapy.all import *
import time
import random
import os
import sys

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
        p1 = os.popen('echo "trigger" | nc -cu '+ soundobject + ' 10000')
        output = p1.read()


def buildup():
    running = True
    timeout = 1
    if(sys.argv[1]=="machine-1"):
        target = "192.168.8.228"
    if(sys.argv[1]=="machine-2"):
        target = "192.168.8.170"
    if(sys.argv[1]=="machine-3"):
        target = "192.168.8.169"
    if(sys.argv[1]=="machine-4"):
        target = "192.168.8.155"
    if(sys.argv[1]=="machine-5"):
        target = "192.168.8.191"
    while running:
            sendPacket(target)
            time.sleep(timeout)
            timeout = timeout - 0.1
            if (timeout < 0.05):
                for x in range (1, 20):
                    sendPacket(target)
                    time.sleep(0.02)
                running = False

def buildup_servo():
    running = True
    timeout = 5

    while running:
        sendPacket(servospring)
        time.sleep(timeout)
        timeout = timeout - 1
        if(timeout < 1):
            for x in range (1, 5):
                sendPacket(servospring)
                time.sleep(1)
            running = False


def buildup_everyone():
    running = True
    timeout = 1

    while running:
        sendPacket("192.168.8.228")
        sendPacket("192.168.8.170")
        sendPacket("192.168.8.169")
        sendPacket("192.168.8.155")
        sendPacket("192.168.8.191")

        if(timeout < 0.05):
            for x in range (1, 20):
                sendPacket("192.168.8.228")
                sendPacket("192.168.8.170")
                sendPacket("192.168.8.169")
                sendPacket("192.168.8.155")
                sendPacket("192.168.8.191")
                time.sleep(0.02)
            running = False

if (sys.argv[1] == "everyone"):
    buildup_everyone()
else:
    buildup()
