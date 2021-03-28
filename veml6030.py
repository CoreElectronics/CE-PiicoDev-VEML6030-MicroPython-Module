# A simple class to read data from the VEML i2c light sensor

# This module has been tested with the following development boards:
#    • BBC Micro:bit
#    • Raspberry Pi Pico (RP2040)

# No warranties express or implied, including any warranty of merchantability and warranty of fitness for a particular purpose.
# Written by Michael Ruppe at Core Electronics MAR 2021

import os
_SYSNAME = os.uname().sysname
# Registers
_veml6030Address = 0x10
_ALS_CONF = b'\x00'
_REG_ALS = b'\x04'

if _SYSNAME == 'microbit':
    from microbit import i2c
else:
    from machine import I2C
    i2c = I2C(0)
    
class VEML6030(object):    
    def __init__(self, addr=_veml6030Address, i2c_=i2c):
        self.i2c = i2c_
        self.addr = addr
        self.res = 0.0288 # lx/bit
        try:
            if _SYSNAME == 'microbit':
                self.i2cWrite = self.i2c.write
                self.i2cRead = self.i2c.read
                self.repeat = True # 3rd parameter in write must be true
            else:
                self.i2cWrite = self.i2c.writeto
                self.i2cRead = self.i2c.readfrom
                self.repeat = False # 3rd parameter in write must be false
        
            self.i2cWrite(self.addr, _ALS_CONF + 'b\x00') # initialise gain:1x, integration 100ms, persistence 1, disable interrupt
        except Exception:
            print('Device 0x{:02X} not found'.format(self.addr))
            
        
    def read(self):
        self.i2cWrite(self.addr, _REG_ALS, self.repeat)
        data = self.i2cRead(self.addr, 2) # returns a bytes object
        return int.from_bytes(data, 'little') * self.res
          
