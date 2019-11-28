#!/usr/bin/env python3
from scapy.all import *
import time
import random

node_num=6
while True:
    random_Number = random.randint(1,node_num)
    for node in range(1,node_num):
        if random_Number == 1:
            send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="Woodblock"))
        if random_Number == 2:
            send(IP(dst="192.168.8.170")/UDP(dport=10000)/Raw(load="Spring solenoid "))
        if random_Number == 3:
            send(IP(dst="192.168.8.169")/UDP(dport=10000)/Raw(load="Copper solenoid "))
        if random_Number == 4:
            send(IP(dst="192.168.8.155")/UDP(dport=10000)/Raw(load="servo;\n"))
        if random_Number == 5:
            send(IP(dst="192.168.8.191")/UDP(dport=10000)/Raw(load="Coffe tin "))
        if random_Number == 6:
            send(IP(dst="192.168.8.255")/UDP(dport=10000)/Raw(load="All"))
        #if random_Number == 7:
        #    print("No send")
        time.sleep(random.random()/7)
