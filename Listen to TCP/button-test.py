#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
import RPi.GPIO as GPIO
from time import sleep

button = Button(2)
SOL = 0
SOL_ACK = 17
SOL_SYN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOL, GPIO.OUT)
GPIO.setup(SOL_SYN, GPIO.OUT)
GPIO.setup(SOL_ACK, GPIO.OUT)

def triggerSol():
    GPIO.output(SOL_SYN, 1)
    sleep(0.05)
    GPIO.output(SOL_SYN, 0)
    sleep(0.1)
    GPIO.output(SOL_ACK, 1)
    sleep(0.05)
    GPIO.output(SOL_ACK, 0)
    
    print("I'm triggered.")

def triggerSYN():
    GPIO.output(SOL_SYN, 1)
    sleep(0.05)
    GPIO.output(SOL_SYN, 0)
    print("I'm triggered SYN.")

def triggerACK():
    GPIO.output(SOL_ACK, 1)
    sleep(0.05)
    GPIO.output(SOL_ACK, 0)
    
    print("I'm triggered ACK.")
button.when_pressed = triggerSol
pause()
