#!/usr/bin/env python3

from gpiozero import Servo

servo = Servo(21)
servoPosition = "low"
class ServoMotor(object):

    def __init__(self, pin):
        servo = Servo(pin)
        print("Servo is on pin " + str(pin))
        self.position = position

    def sweep(self):
        if self.position == "low":
            servo.min()
            self.position =  "high"
        else:
            servo.max()
            self.position = "low"


def swipe():
    global servoPosition
    if servoPosition == "low":
        servo.min()
        servoPosition =  "high"
    else:
        servo.max()
        servoPosition = "low"


