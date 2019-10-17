#!/usr/bin/env python3
from scapy.all import *
import time
import random

while True:
    random_Number = random.randint(1,2)
    for node in range(1,2):
        if random_Number == 1:
            send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="Hi!"))
        if random_Number == 4:
           send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="servo;\n"))
        time.sleep(random.random()/2)
