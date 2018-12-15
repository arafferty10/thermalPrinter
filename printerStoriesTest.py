#Aidan Rafferty
#Thermal Printer Longer story test
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
        # n = 0
        # n = random.randint(1,4)
        print('Button Pressed')
        # print(n)
        time.sleep(0.4)

        printer.feed(2)
        printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
        printer.size = adafruit_thermal_printer.SIZE_LARGE
        printer.print('Dimension')
        printer.size = adafruit_thermal_printer.SIZE_MEDIUM
        printer.print('By Alice Murno')
        printer.feed(2)
        printer.justify = adafruit_thermal_printer.JUSTIFY_LEFT
        printer.size = adafruit_thermal_printer.SIZE_SMALL
        printer.print('Doree had to take three buses—one to Kincardine, where she waited for one to London, where she waited again, for the city bus out to the facility. She started the trip on a Sunday at nine in the morning. Because of the waiting times between buses, it took her until about two in the afternoon to travel the hundred-odd miles. All that sitting, either on buses or in the depots, was not a thing she should have minded. Her daily work was not of the sitting-down kind. She was a chambermaid at the Comfort Inn. She scrubbed bathrooms and stripped and made beds and vacuumed rugs and wiped mirrors. She liked the work—it occupied her thoughts to a certain extent and tired her out so that she could sleep at night. She was seldom faced with a really bad mess, though some of the women she worked with could tell stories to make your hair curl. These women were older than her, and they all thought that she should try to work her way up. They told her that she should get trained for a job behind the desk, while she was still young and decent-looking. But she was content to do what she did. She didn’t want to have to talk to people.')
        printer.feed(2)
