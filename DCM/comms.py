import serial 
import struct 
from PyQt5.QtCore import pyqtSignal, QThread

class serialThreadClass(QThread):
	
	def __init__(self):
		super(serialThreadClass, self).__init__()
		self.ser = serial.Serial()
		self.ser.baudrate = 115200
		self.ser.port = "COM8"
		self.ser.timeout = 10

	def open_serial(self):
		self.ser.open()
		if(self.ser.isOpen()):
			print("Opened: "+ self.ser.port)

	def close_serial(self):
		self.ser.close()
		print("Closed: "+ self.ser.port)

	def get_data(self,size):
		temp = ['0', '0', '0', '0','0', '0', '0','0', '0', '0', '0','0', '0', '0', '0']
		if(size == 15):
			#uint8
			for i in range(0,8):
				temp[i] = self.ser.readline(1)
				temp[i]= str(int.from_bytes(temp[i],'little'))
				print(temp[i])
			# uint16
			for i in range(8,11):
				temp[i] = self.ser.readline(2)
				temp[i] = struct.unpack('<h', temp[i])
				temp[i] = str(temp[i][0])
				print(temp[i])
			# single
			for i in range(11,15):
				temp[i] = self.ser.readline(4)
				temp[i] = struct.unpack('<f', temp[i])
				temp[i] = str(temp[i][0])
				print(temp[i])

		print(temp)
		return temp

	def send_data(self,param_list):
		
		for param in param_list:
			if(param.isdigit()):
				if(int(param)>=256):
					param = struct.pack('<h',int(param))
					print([ "0x%02x" % b for b in param])
				else:
					param = bytes([int(param)])
					print(param)
			else:
				param = struct.pack('<f',float(param))
				print([ "0x%02x" % b for b in param])
				print(param)

			self.ser.write(param)

