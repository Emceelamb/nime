#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep
import time

class Solenoid(object):
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
#        print("Solenoid is set to " + str(self.pin))

    def trigger(self):
#        timeout = int(round(time.time() * 1000))+100
        GPIO.output(self.pin, 1)
#        while (int(round(time.time() * 1000))) < timeout:
#            getTime = int(round(time.time()))
        time.sleep(0.01)
        GPIO.output(self.pin, 0)
        
