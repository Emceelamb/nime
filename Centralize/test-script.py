#!/usr/bin/env python3
from scapy.all import *
import time
import random

while True:
#    random_Number = random.randint(1,3)
    for node in range(1,3):
        if random_Number == 1:
            send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="Hi!"))
        if random_Number == 2:
            send(IP(dst="192.168.8.170")/UDP(dport=10000)/Raw(load="Hi!"))
        if random_Number == 3:
           send(IP(dst="192.168.8.169")/UDP(dport=10000)/Raw(load="Hi!"))
        time.sleep(0.5)
