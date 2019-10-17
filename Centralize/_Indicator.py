#!/usr/bin/env python2
from gpiozero import RGBLED
from time import sleep
import time

led = RGBLED(red=22, green=9, blue=10)
class Indicator(object):
#    led = RGBLED(red=22, green=9, blue=10)

    def __init__(self, color):
        self.start_led_fade = False
        self.color = color

    def led_fade(self):
        self.start_led_fade = True

    def led_on(self):
        led.color = (1,1,1)
       
    def led_off(self):
        led.color = (0,1,1)

    def fadeIn(self, start, end, percent):
        if self.color == 'red':
            led.red = lerp(self, start, end, percent)/end


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

def lerp(self, start, end, percent):
    return (start + percent * (end-start))

