#!/usr/bin/env python3
from gpiozero import RGBLED
import time

led = RGBLED(red=22, green=9, blue=10)
class Indicator(object):
#    led = RGBLED(red=22, green=9, blue=10)

    def __init__(self, color):
        self.color = color

    def fadeIn(self):
        if self.color == 'red':
            led.red = 0

        if self.color == 'green':
            for i in range(10):
                led.green = i/10

        if self.color == 'blue':
            for i in range(10):
                led.blue = i/10

    def fadeOut(self):
        if self.color == 'red':
            for i in range(10,0,-1):
                led.red = 10-i/10

        if self.color == 'green':
            for i in range(10):
                led.green = i/10

        if self.color == 'blue':
            for i in range(10):
                led.blue = i/10
