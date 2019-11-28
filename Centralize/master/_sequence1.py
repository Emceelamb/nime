#!/usr/bin/env python3
from scapy.all import *
import time
import random

START_TIME = time.time()
s = conf.L3socket(iface='enp60s0')

woodblock = "192.168.8.228"
coffeetin = "192.168.8.191"
goldtin = "192.168.8.170"
woodspring = "192.168.8.169"
servospring = "192.168.8.155"

def sendPackets(c=1, i=0):
    s.send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="Trigger"), realtime=1, count=c, inter=i)

def sendPacket(soundobject):
    pkt=IP(dst=soundobject)/UDP(dport=10000)/Raw(load="Trigger")
    s.send(pkt)

def buildup():
    running = True
    timelapse = 1
    prevTime = START_TIME
    sendPacket(woodblock)

    while running:
        sendPacket(woodblock)
        time.sleep(timelapse)
        timelapse = timelapse - 0.1
        if timelapse < 0.2:
            for x in range (1,20):
                sendPacket(woodblock)
                time.sleep(timelapse)
            running = False


buildup()

"""
while True:
    random_Number = random.randint(1,6)
    for node in range(1,6):
        if random_Number == 1:
            send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="Trigger"))
        if random_Number == 2:
            send(IP(dst="192.168.8.170")/UDP(dport=10000)/Raw(load="Trigger"))
        if random_Number == 3:
           send(IP(dst="192.168.8.169")/UDP(dport=10000)/Raw(load="Trigger!"))
        if random_Number == 4:
           send(IP(dst="192.168.8.155")/UDP(dport=10000)/Raw(load="servo;\n"))
        if random_Number == 5:
           send(IP(dst="192.168.8.191")/UDP(dport=10000)/Raw(load="Trigger tin"))
        if random_Number == 6:
           send(IP(dst="192.168.8.255")/UDP(dport=10000)/Raw(load="servo;\n"))
        time.sleep(random.random()/10)
"""
