#Aidan Rafferty
#Thermal Printer Button and Random Integer Test
#https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython
#Winter 2018

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
        n = random.randint(1,4)
        print('Button Pressed')
        print(n)
        time.sleep(0.4)

        if n == 1:
            printer.feed(1)
            printer.print("Choice 1: Help I'm stuck in the printer")
            printer.feed(3)
        elif n == 2:
            printer.feed(1)
            printer.bold = True
            printer.print('cHoIcE 2: Do or do not there is no try!')
            printer.bold = False
            printer.feed(3)
        elif n == 3:
            printer.feed(1)
            printer.underline = adafruit_thermal_printer.UNDERLINE_THICK
            printer.bold = True
            printer.print('#3: I WILL DESTROY YOU!!!')
            printer.underline = None
            printer.bold = False
            printer.feed(3)
        elif n == 4:
            printer.feed(1)
            printer.double_height = True
            printer.print('Selection 4: Commander Cody, Execute Order 66!')
            printer.double_height = False
            printer.feed(3)


print("Code Complete!")
