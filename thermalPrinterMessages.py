#Aidan Rafferty
#Thermal Printer Messages for implementation
#https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython
#Spring 2019

import board
import busio
import serial
import adafruit_thermal_printer
import RPi.GPIO as GPIO
import time
import random

#--------------------SETUP------------------------
#Set values for button
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Initialize hardware serial connection to the printer
uart = serial.Serial("../../../dev/serial0", baudrate=19200, timeout=3000)

#Create Thermal Printer Class
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.68)
printer = ThermalPrinter(uart)

#-------------------------------------------------

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        n = 0
        n = random.randint(1,3)
        print('Button Pressed')
        print(n)
        time.sleep(0.4)

        if n == 1:
            printer.feed(2)

            storyStr = ''
            #Ignores ascii characters for printing
            storyStr = storyStr.encode('ascii', 'ignore').decode('ascii')

            printer.print(storyStr)
            printer.feed(2)

        if n == 2:
            printer.feed(2)

            storyStr = ''
            #Ignores ascii characters for printing
            storyStr = storyStr.encode('ascii', 'ignore').decode('ascii')

            printer.print(storyStr)
            printer.feed(2)

        if n == 3:

            storyStr = ''
            #Ignores ascii characters for printing
            storyStr = storyStr.encode('ascii', 'ignore').decode('ascii')

            printer.print(storyStr)
            printer.feed(2)
