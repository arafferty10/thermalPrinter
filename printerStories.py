#Aidan Rafferty
#Thermal Printer Choosing a Random Story
#https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython
#Winter 2018

import board
import busio
import serial
import adafruit_thermal_printer

#Create Value to choose Story
n = 0

#Initialize hardware serial connection to the printer
uart = serial.Serial("../../../dev/serial0", baudrate=19200, timeout=3000)

#Create Thermal Printer Class
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.68)

printer = ThermalPrinter(uart)

#Should be ready to print now :)
#Printing a full test page
# printer.test_page()

#printer.feed() advances the paper forward some lines given
printer.feed(3)

printer.print("Hello World! I'm Alive!")
printer.feed(3)

print("Code Complete!")
