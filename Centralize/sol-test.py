#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
from TriggerSolenoid import *

button = Button(3)
sol = Solenoid(4)

button.when_pressed = sol.trigger
pause()
