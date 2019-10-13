#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
from TriggerSolenoid import *
from Indicator import *

button = Button(3)
solenoid = Solenoid(4)

indicator = Indicator("red")

button.when_pressed = solenoid.trigger
#button.when_pressed = indicator.fadeIn
pause()
