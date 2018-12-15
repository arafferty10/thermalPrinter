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
        n = 0
        n = random.randint(1,3)
        print('Button Pressed')
        print(n)
        time.sleep(0.4)

        if n == 1:
            printer.feed(2)
            printer.size = adafruit_thermal_printer.SIZE_MEDIUM
            printer.print('The Fruit of My Woman')
            printer.size = adafruit_thermal_printer.SIZE_MEDIUM
            printer.print('By Han Kang\n')
            printer.size = adafruit_thermal_printer.SIZE_SMALL

            storyStr = 'I struggled to recall the last occasion that I’d seen my wife naked, and it had been bright enough to see her properly. Not that year, for sure; I wasn’t even certain that it had happened the year before. How could I have failed to notice such deep bruises on the body of the only person I lived with? I tried to count the fine wrinkles radiating out from the corners of my wife’s eyes. Then I told her to take off all her clothes. A red flush appeared along the line of her cheekbones, which her weight loss had left indecently sharp. She tried to remonstrate with me. ‘What if someone sees?’'
            #Ignores ascii characters for printing
            storyStr = storyStr.encode('ascii', 'ignore').decode('ascii')

            printer.print(storyStr)
            printer.feed(2)

        elif n == 2:
            printer.feed(2)
            printer.size = adafruit_thermal_printer.SIZE_MEDIUM
            printer.print('The Proxy Marriage')
            printer.size = adafruit_thermal_printer.SIZE_MEDIUM
            printer.print('By Maile Meloy\n')
            printer.size = adafruit_thermal_printer.SIZE_SMALL

            storyStr = 'William had no girlfriends in high school, and his mother once sat him down at the table in her spotless kitchen and asked if he was gay. She said it would be fine with her. She loved him unconditionally, and they would figure out a way to tell his father. But William wasn’t gay. He was just absurdly, painfully in love with Bridey Taylor, who leaned on the piano and sang while he played, and he had no way of telling her. He was too shy to pursue other girls, even when the payoff seemed either likely or worth the agony. But he didn’t tell his mother that. It was too humiliating. He just stammered an unconvincing denial.'
            storyStr = storyStr.encode('ascii', 'ignore').decode('ascii')

            printer.print(storyStr)
            printer.feed(2)

        elif n == 3:
            printer.feed(2)
            printer.size = adafruit_thermal_printer.SIZE_MEDIUM
            printer.print('Axis of Happiness')
            printer.size = adafruit_thermal_printer.SIZE_MEDIUM
            printer.print('By Min Jin Lee\n')
            printer.size = adafruit_thermal_printer.SIZE_SMALL

            storyStr = 'The morning Henry Evans stopped by my office to tell me to go to Chicago, I was in the middle of my chapter-a-day habit: still in the Book of Hosea, much to my dismay, still in the Old Testament after years of dogged reading. This habit required skimming the day’s chapter of the Bible (usually the length of one onion-skin page), then reading the extensive commentaries in the footnotes, then finally reading the chapter again—all of this took on average forty-five minutes. I did this at work because it was where I lived—fourteen hours a day, often six days a week. I couldn’t help knowing some of the Bible because I was a P.K. (preacher’s kid), but I’d started reading this fat copy of the NIV Study Bible with its elephant-gray leather cover because my mother left it for me along with her modest wedding jewelry when she died three years ago.'
            storyStr = storyStr.encode('ascii', 'ignore').decode('ascii')

            printer.print(storyStr)
            printer.feed(2)
