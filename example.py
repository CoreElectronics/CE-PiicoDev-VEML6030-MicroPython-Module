# PiicoDev VEML6030 minimal example code
# This program reads light data from the PiicoDev VEML6030 ambient light sensor
# and displays the result

from veml6030 import *
from utime import sleep_ms

sensor = VEML6030()

while True:
    # Read and print light data
    lightVal = sensor.read()
    print("{} lux".format(lightVal)) # Open the plotter (View > Plotter) to observe light changing over time
    
    sleep_ms(1000)