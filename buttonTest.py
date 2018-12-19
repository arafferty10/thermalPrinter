#Aidan Rafferty
#Thermal Printer Button Test
#https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython
#Winter 2018

import board
import busio
import serial
import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        n = 0
        n = random.randint(1,10)
        print('Button Pressed')
        print(n)
        time.sleep(0.4)
        printer.feed(3)
        printer.print("Hi Baby!\n")
        printer.print("I lervvvv you!\n")
        printer.print("From, Your nor so Secret Admirer")
        printer.feed(3)
