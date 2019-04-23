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
        n = random.randint(1,12)
        print('Button Pressed')
        print(n)
        time.sleep(0.4)

        if n == 1:
            printer.feed(2)

            msg = 'I love you soooooo much baby!! I hope you have a fantastic day! :))) \n -Aidan'
            #Ignores ascii characters for printing
            msgStr = msg.encode('ascii', 'ignore').decode('ascii')

            printer.print(msgStr)
            printer.feed(2)

        if n == 2:
            printer.feed(2)

            msg = 'Sending all my love to my most speical person in the whole wide world! \n -Aidan'
            #Ignores ascii characters for printing
            msgStr = msg.encode('ascii', 'ignore').decode('ascii')

            printer.print(msgStr)
            printer.feed(2)

        if n == 3:
            printer.feed(2)

            msg = 'You are the most speical, most wonderful person in the entire world! I cant imagine what my life would be without you, I love you Joely <3 \n -Aidan'
            #Ignores ascii characters for printing
            msgStr = msg.encode('ascii', 'ignore').decode('ascii')

            printer.print(msgStr)
            printer.feed(2)

        if n == 4:
            printer.feed(2)

            msg = 'MEMBER SHANGHAI!!! MEMBER MOAB!!! MEMBER EUROPE!!! Youre my absolute favorite travel buddy and I cannot wait to see the entire world with you my love! \n -Aidan'
            msgStr = msg.encode('ascii', 'ignore').decode('ascii')

            printer.print(msgStr)
            printer.feed(2)

        if n == 5:
            printer.feed(2)

            msg = 'I feel very blessed to have a partner in life who supports me, who is enthusiastic about what I want to do. - Hillary Clinton \n This is how I feel about you every day Joely, I love you :) \n -Aidan'
            msgStr = msg.encode('ascii', 'ignore').decode('ascii')

            printer.print(msgStr)
            printer.feed(2)

        if n == 6:
            printer.feed(2)

            msg = 'Youre always on my mind my love! Have a fantastic day!! \n -Aidan'
            msgStr = msg.encode('ascii', 'ignore').decode('ascii')

            printer.print(msgStr)
            printer.feed(2)

        if n == 7:
            printer.feed(2)

            msg = 'I lerv you babyyyyy!! \n -Aidan'
            msgStr = msg.encode('ascii', 'ignore').decode('ascii')

            printer.print(msgStr)
            printer.feed(2)

        if n == 8:
            printer.feed(2)

            msg = "You're so dope and sweet \n -Aidan"
            msgStr = msg.encode('ascii', 'ignore').decode('ascii')

            printer.print(msgStr)
            printer.feed(2)

        if n == 9:
            printer.feed(2)

            msg = 'Joely Tynes is the bombbbbb \n -Your Robot Printer Admirier'
            msgStr = msg.encode('ascii', 'ignore').decode('ascii')

            printer.print(msgStr)
            printer.feed(2)

        if n == 10:
            printer.feed(2)

            msg = "You're the best my babeee! \n From, Your not so secret admirier"
            msgStr = msg.encode('ascii', 'ignore').decode('ascii')

            printer.print(msgStr)
            printer.feed(2)

        if n == 11:
            printer.feed(2)

            msg = '\n -Aidan'
            msgStr = msg.encode('ascii', 'ignore').decode('ascii')

            printer.print(msgStr)
            printer.feed(2)

        if n == 12:
            printer.feed(2)

            msg = '\n -Aidan'
            msgStr = msg.encode('ascii', 'ignore').decode('ascii')

            printer.print(msgStr)
            printer.feed(2)
