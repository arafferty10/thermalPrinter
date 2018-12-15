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
        printer.size = adafruit_thermal_printer.SIZE_LARGE
        printer.print('The Fruit of My Woman')
        printer.size = adafruit_thermal_printer.SIZE_MEDIUM
        printer.print('By Han Kang')
        printer.size = adafruit_thermal_printer.SIZE_SMALL
        printer.print('I struggled to recall the last occasion that I’d seen my wife naked, and it had been bright enough to see her properly. Not that year, for sure; I wasn’t even certain that it had happened the year before. How could I have failed to notice such deep bruises on the body of the only person I lived with? I tried to count the fine wrinkles radiating out from the corners of my wife’s eyes. Then I told her to take off all her clothes. A red flush appeared along the line of her cheekbones, which her weight loss had left indecently sharp. She tried to remonstrate with me. ‘What if someone sees?’')
        printer.feed(2)
