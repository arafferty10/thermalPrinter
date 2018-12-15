#Aidan Rafferty
#Thermal Printer Button Test
#https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython
#Winter 2018

import board
import busio
import serial
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)