#!/usr/bin/env python3

import time, os, sys
from button import *
from TriggerSolenoid import * 

fname = "tmp.txt"
f = open("tmp.txt", "r")
logfile = os.fstat(f.fileno()).st_ino

SYN = Solenoid(4)
ACK = Solenoid(17)

while True:
    while True:
        buf = f.read(1024)
        if buf =="":
            break
        packets = buf.splitlines()

        for i in range(len(packets)):
            line = packets[i].strip()
            parsedLine = line.split(' ')
            lineLen = len(parsedLine)
            # print(lineLen, line)
            if lineLen == 19:
                pTime = parsedLine[1]
                ipDst = parsedLine[4]
                pType = "SYN"
                parsedPacket = [pTime, ipDst, pType]
                print("Sync request sent to " + ipDst)
                SYN.trigger()
            if lineLen == 21:
                pTime = parsedLine[1]
                ipDst = parsedLine[4]
                pType = "SYN ACK"
                parsedPacket = [pTime, ipDst, pType]
                
                print("Acknowledged by " + ipDst)
                ACK.trigger()
            

    try:
        if os.stat(fname).st_ino != logfile:
            new = open("tmp.txt", "r")
            f.close()
            f = new
            logfile = os.fstat(f.fileno()).st_ino
            continue
    except IOError:
        pass
    time.sleep(1)

