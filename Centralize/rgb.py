#!/usr/bin/env python3
from gpiozero import RGBLED
from time import sleep

class light(object):
    d
led = RGBLED(red=22, green=9, blue=10)

led.color = (0,1,1)

def dim:
    color = 'red'
    def __init__(self, color):
        self.color = color
        if self.color == 'red'
            color = 'red'
        if self.color == 'green'
            color = 'green'
        if self.color == 'blue'

    def fade:
        for i in range(10):
            led.color = i/10
            sleep(0.1)


