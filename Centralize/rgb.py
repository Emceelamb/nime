#!/usr/bin/env python3
from gpiozero import RGBLED
from time import sleep

class light(object):
    led = RGBLED(red=22, green=9, blue=10)

    def __init__(self, color):
        self.color = color

    def fadeIn():
        if self.color == 'red':
            for i in range(10):
                led.red = i/10
                sleep(0.1)

        if self.color == 'green':
            for i in range(10):
                led.green = i/10
                sleep(0.1)

        if self.color == 'blue':
            for i in range(10):
                led.blue = i/10
                sleep(0.1)

    def fadeOut():
        if self.color == 'red':
            for i in range(10,0):
                led.red = i/10
                sleep(0.1)

        if self.color == 'green':
            for i in range(10):
                led.green = i/10
                sleep(0.1)

        if self.color == 'blue':
            for i in range(10):
                led.blue = i/10
                sleep(0.1)

led = light('red')
led.fadeIn
