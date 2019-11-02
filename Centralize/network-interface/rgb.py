#!/bin/env python3

from gpiozero import RGBLED

led = RGBLED(red=9, green=10, blue=11)
led.red=0
