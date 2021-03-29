# PiicoDev VEML6030 minimal example code
# This program reads light data from the PiicoDev VEML6030 ambient light sensor
# and displays the result

from veml6030 import *
from utime import sleep_ms

# Initialise Sensor
sensor = VEML6030()

while True:
    # Read and print light data
    lightVal = sensor.read()
    print("{} lux".format(lightVal))
    
    sleep_ms(1000)