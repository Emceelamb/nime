#!/usr/bin/env python3
from scapy.all import *
import time
import random
import os
import sys
import threading


machine1 = "192.168.8.228"
machine2 = "192.168.8.170"
machine3 = "192.168.8.169"
machine4 = "192.168.8.155"
machine5 = "192.168.8.191"
everyone = "everyone"

def thread_func():
    print ("start thread")

#interval = sys.argv[1]
#repetition = sys.argv[2]

def sendPackets(c=1, i=0):
    s.send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="Trigger"), realtime=1, count=c, inter=i)

def sendPacket(soundobject):
    if soundobject == machine4:
        p1 = os.popen('echo "servo;\n" | nc -cu '+ soundobject + ' 10000')
        output = p1.read()
    
    elif soundobject == "everyone":
        p1 = os.popen('echo "trigger" | nc -cu '+ machine1 + ' 10000')
        output = p1.read()
        p2 = os.popen('echo "trigger" | nc -cu '+ machine2 + ' 10000')
        output2 = p2.read()
        p3 = os.popen('echo "trigger" | nc -cu '+ machine3 + ' 10000')
        output3 = p3.read()
        p4 = os.popen('echo "trigger" | nc -cu '+ machine4 + ' 10000')
        output4 = p4.read()
        p5 = os.popen('echo "trigger" | nc -cu '+ machine5 + ' 10000')
        output5 = p5.read()
    else:
        p1 = os.popen('echo "trigger" | nc -cu '+ soundobject + ' 10000')
        output = p1.read()



def send(c, r, i):
    for x in range (1, r):
        sendPacket(c)
        time.sleep(i)

def hello(c,r,i):
    thread = threading.Thread(target=send, args=(c, r, i))
    thread.start()
