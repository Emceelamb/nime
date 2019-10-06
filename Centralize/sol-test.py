#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
from TriggerSolenoid import *
import rgb

button = Button(3)
sol = Solenoid(4)

indicator = new rgb.light(red)

button.when_pressed = sol.trigger
button.when_press = indicator.fadeIn
pause()
