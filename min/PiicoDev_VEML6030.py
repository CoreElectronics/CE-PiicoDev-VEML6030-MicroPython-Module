_B='little'
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
		self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.addr=addr;self.gain=1;self.res=0.0576;self.i2c.writeto_mem(self.addr,_ALS_CONF,_DEFAULT_SETTINGS);sleep_ms(4)
	def read(self):
		try:data=self.i2c.readfrom_mem(self.addr,_REG_ALS,2)
		except:print(i2c_err_str.format(self.addr));return float('NaN')
		return int.from_bytes(data,_B)*self.res
	def setGain(self,g):
		if g not in[0.125,0.25,1,2]:raise ValueError('Invalid gain. Accepted values: 0.125, 0.25, 1, 2')
		self.gain=g
		if g==0.125:conf=b'\x00\x10';self.res=0.4608
		if g==0.25:conf=b'\x00\x18';self.res=0.2304
		if g==1:conf=b'\x00\x00';self.res=0.0576
		if g==2:conf=b'\x00\x08';self.res=0.0288
		self.setBits(_ALS_CONF,conf,'b\x18\x00');sleep_ms(4);return
	def setBits(self,address,byte,mask):
		old=self.i2c.readfrom_mem(self.addr,address,2);old_byte=int.from_bytes(self.i2c.readfrom_mem(self.addr,address,2),_B);temp_byte=old_byte;int_byte=int.from_bytes(byte,_B);int_mask=int.from_bytes(mask,'big')
		for n in range(16):
			bit_mask=int_mask>>n&1
			if bit_mask==1:
				if int_byte>>n&1==1:temp_byte=temp_byte|1<<n
				else:temp_byte=temp_byte&~(1<<n)
		new_byte=temp_byte;print(new_byte);self.i2c.writeto_mem(self.addr,address,new_byte.to_bytes(2,_B))