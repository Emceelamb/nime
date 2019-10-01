#!/usr/bin/env python3
from gpiozero import RGBLED
from signal import pause
from time import sleep
import RPi.GPIO as GPIO

led = RGBLED(red=22, green=9, blue=10)

led.color = (0,1,1)

for i in range(10):
    led.red = i/10
    sleep(0.1)


