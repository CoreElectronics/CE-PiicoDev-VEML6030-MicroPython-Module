# PiicoDev VEML6030 minimal example code
# This program reads light data from the PiicoDev VEML6030 ambient light sensor
# and displays the result

from PiicoDev_VEML6030 import PiicoDev_VEML6030, sleep_ms

# Initialise Sensor
light = PiicoDev_VEML6030()

while True:
    # Read and print light data
    lightVal = light.read()
    print(str(lightVal) + " lux")
    
    sleep_ms(1000)