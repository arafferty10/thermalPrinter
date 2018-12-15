#Aidan Rafferty
#Thermal Printer First Test
#https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython
#Winter 2018

import board
import busio
import serial
import adafruit_thermal_printer

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

#----------------------PRINTER FONTS-------------------------
#printer.bold = True ---> turns on bold text
#printer.inverse = True ---> Prints white on black text
#printer.upside_down = True ---> Prints text upside upside down
#printer.double_height = True ---> Doubles text height size
#printer.double_width = True ---> Doubles text width size
#printer.strike = True ---> Prints text with strike through
#-------------------------------------------------------------

#EXAMPLE TO PRINT THICK UNDERLINED, MEDIUM TEXT, W/CENTER JUSTIFY
#Some properties can set to special values to further control text printing
#-----------------------------------------------------------------
# printer.underline = adafruit_thermal_printer.UNDERLINE_THICK
# printer.size = adafruit_thermal_printer.SIZE_MEDIUM
# printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
# printer.print('Medium center!')
# # Reset back to normal printing:
# printer.underline = None
# printer.size = adafruit_thermal_printer.SIZE_SMALL
# printer.justify = adafruit_thermal_printer.JUSTIFY_LEFT
#-----------------------------------------------------------------
