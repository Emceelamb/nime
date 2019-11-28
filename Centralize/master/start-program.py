#!/usr/bin/env python3
from scapy.all import *
import time
import random


while True:
    send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="Trigger"))
    # time.sleep(0.5)
    send(IP(dst="192.168.8.170")/UDP(dport=10000)/Raw(load="Trigger"))
    # time.sleep(0.5)
    send(IP(dst="192.168.8.169")/UDP(dport=10000)/Raw(load="Trigger!"))
    # time.sleep(0.5)
    send(IP(dst="192.168.8.155")/UDP(dport=10000)/Raw(load="Trigger"))
    # time.sleep(0.5)
    send(IP(dst="192.168.8.191")/UDP(dport=10000)/Raw(load="Message"))
    # time.sleep(0.5)
    
    send(IP(dst="192.168.8.228")/UDP(dport=10000)/Raw(load="Trigger"))
    # time.sleep(0.5)
    send(IP(dst="192.168.8.170")/UDP(dport=10000)/Raw(load="Trigger"))
    # time.sleep(0.5)
    send(IP(dst="192.168.8.169")/UDP(dport=10000)/Raw(load="Trigger!"))
    # time.sleep(0.5)
    send(IP(dst="192.168.8.155")/UDP(dport=10000)/Raw(load="Trigger"))
    # time.sleep(0.5)
    send(IP(dst="192.168.8.191")/UDP(dport=10000)/Raw(load="Message"))
    # time.sleep(0.5)
    
    
    
    send(IP(dst="192.168.8.255")/UDP(dport=10000)/Raw(load="servo;\n"))
    time.sleep(0.5)
    send(IP(dst="192.168.8.255")/UDP(dport=10000)/Raw(load="servo;\n"))
    time.sleep(0.5)
    send(IP(dst="192.168.8.255")/UDP(dport=10000)/Raw(load="servo;\n"))
