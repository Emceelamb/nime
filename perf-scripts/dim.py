from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=22, green=9, blue=10)


for n in range(100):
    led.red = n/10
    sleep(0.1)


