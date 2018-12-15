#Aidan Rafferty
#Thermal Printer Choosing a Random Story
#https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython
#Winter 2018

import board
import busio
import serial
import adafruit_thermal_printer
import RPi.GPIO as GPIO
import time

#Set values for button
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Initialize hardware serial connection to the printer
uart = serial.Serial("../../../dev/serial0", baudrate=19200, timeout=3000)

#Create Thermal Printer Class
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.68)

printer = ThermalPrinter(uart)

#printer.feed() advances the paper forward some lines given
printer.feed(5)

printer.print("Hello World! I'm Alive!")
printer.feed(3)

print("Code Complete!")
