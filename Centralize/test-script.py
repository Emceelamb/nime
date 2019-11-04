#!/usr/bin/env python3
from scapy.all import *
import time
import random

while True:
    random_Number = random.randint(1,4)
    for node in range(1,4):
        if random_Number == 1:
            send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="Trigger"))
        if random_Number == 2:
            send(IP(dst="192.168.8.170")/UDP(dport=10000)/Raw(load="Trigger"))
        if random_Number == 3:
           send(IP(dst="192.168.8.169")/UDP(dport=10000)/Raw(load="Trigger!"))
        if random_Number == 4:
           send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="servo;\n"))
        time.sleep(random.random()/4)
