#Testing ability to retrieve daily horoscope
#################Currently works only in python 2.7####################

import pyaztro

horoscope = pyaztro.Aztro(sign='aries')
hor = horoscope.description

print(hor)
