_A=None
from PiicoDev_Unified import *
compat_str='\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'
_veml6030Address=16
_ALS_CONF=0
_REG_ALS=4
_DEFAULT_SETTINGS=b'\x00'
class PiicoDev_VEML6030:
	def __init__(self,bus=_A,freq=_A,sda=_A,scl=_A,addr=_veml6030Address):
		try:
			if compat_ind>=1:0
			else:print(compat_str)
		except:print(compat_str)
		self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.addr=addr;self.res=0.0576;self.i2c.writeto_mem(self.addr,_ALS_CONF,_DEFAULT_SETTINGS)
	def read(self):
		try:data=self.i2c.readfrom_mem(self.addr,_REG_ALS,2)
		except:print(i2c_err_str.format(self.addr));return float('NaN')
		return int.from_bytes(data,'little')*self.res