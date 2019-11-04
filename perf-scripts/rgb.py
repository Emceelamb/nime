from gpiozero import RGBLED
from signal import pause
import time

led = RGBLED(red=22, green=10, blue=9)

led.red = 1

start_time = time.time()
step_time = 0.1

def timer(x):
    previous_time = start_time - 0.1
    current_time = time.time()
    if current_time > previous_time:
        previous_time = previous_time + step_time
        return x - 0.01
    return x

while True:
    if led.red > 0.02:
        led.red = timer(led.red)
        print(led.red)
    else:
        led.red = 1 
        print("reset led")
    
    
