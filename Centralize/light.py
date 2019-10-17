#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
from TriggerSolenoid import *
from gpiozero import RGBLED

button = Button(3)
solenoid = Solenoid(4)

indicator = RGBLED(red=22, green=9, blue=10)
indicator_state = True
indicator.color=(1,1,1)

start_sec = int(time.time()) 
previous_sec = start_sec


def test_both():
    global indicator_state
    solenoid.trigger()
    indicator_state = False 
    #print(indicator_state, "!")

while True:
    elapsed_time = int(time.time()) - start_sec

    if button.is_pressed:
        press_time = int(time.time())
        test_both()
    print(indicator_state)

    if indicator_state == False and int(time.time()) - press_time > 0.5:
        print(int(time.time()) - press_time, 'blah')
        indicator_state = True

    if indicator_state:
        indicator.color = (0,1,1)
    else:
        indicator.color = (1,1,1)





    #elapsed_percent = (time.time() - start_time) / 4
  #Indicator.level( lerp(10, 0, elapsed_time) )
