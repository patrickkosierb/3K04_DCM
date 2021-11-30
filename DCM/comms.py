import serial 
import struct 
from PyQt5.QtCore import pyqtSignal, QThread
import copy
import time

class serialThreadClass(QThread):
	
	def __init__(self):
		super(serialThreadClass, self).__init__()
		self.ser = serial.Serial()
		self.ser.baudrate = 115200
		self.ser.port = "COM7"
		self.ser.timeout = 1

	def open_serial(self):
		try:
			self.ser.open()
			if(self.ser.isOpen()):
				print("Opened: "+ self.ser.port)
		except:
			print("PM not found")

	def isopen(self):
		return self.ser.isOpen()

	def close_serial(self):
		self.ser.close()
		print("Closed: "+ self.ser.port)

	def check_conn(self):
		try:
			sync = bytes([255])
			self.ser.write(sync)
			echo = bytes([1])
			self.ser.write(echo)
			for i in range(0,24):
				buff = bytes([0])
				self.ser.write(buff)
			sync = self.ser.readline(1) # sync
			sync = int.from_bytes(sync,'little')
			print(sync)
			if(sync == 255):
				return 1
			else:
				print("ERROR: Receive Sync. Failure")
				return 0
		except:
			print("PM not found")
			return 0

	def get_param(self):		

		if(self.check_conn()):
			# check function code
			code = self.ser.readline(1)
			code = int.from_bytes(code,'little')
			if(code == 2):
				# receive param
				temp = ['0', '0', '0', '0','0', '0', '0','0', '0', '0', '0','0', '0', '0', '0']
				#uint8
				for i in range(0,10):
					temp[i] = self.ser.readline(1)
					temp[i]= str(int.from_bytes(temp[i],'little'))
				# uint16
				for i in range(10,13):
					temp[i] = self.ser.readline(2)
					temp[i] = struct.unpack('<h', temp[i])
					temp[i] = str(temp[i][0])
				# single
				for i in range(13,15):
					temp[i] = self.ser.readline(4)
					temp[i] = struct.unpack('<f', temp[i])
					temp[i] = temp[i][0]
			
				for i in range(13,15):
					temp[i] = str(round(temp[i],2))
				return temp
				
			else:
				print(code)
				print("ERROR: Receive Func. Error")
				return 0
		else:
			return 0

	def send_data(self,param_list):
		temp = copy.deepcopy(param_list)
		try:
			sync = bytes([255])
			self.ser.write(sync)
			code = bytes([2])
			self.ser.write(code)
			# uint8
			for i in range(0,10):
				temp[i] = bytes([int(temp[i])])
				self.ser.write(temp[i])
			# uint16
			for i in range(10,13):
				temp[i] = struct.pack('<h',int(temp[i]))
				self.ser.write(temp[i])
			# single
			for i in range(13,15):
				temp[i] = struct.pack('<f',float(temp[i]))
				self.ser.write(temp[i])
			time.sleep(2)
			pm_data = self.get_param()
			pm_data[13] = float(pm_data[13])
			pm_data[13]=round(pm_data[13],2)
			pm_data[14] = float(pm_data[14])
			pm_data[14]=round(pm_data[14],2)
			pm_data[13] = str(pm_data[13])
			pm_data[14] = str(pm_data[14])

			if(pm_data == param_list):
				print("Successfully sent data")
				return 1
			else:
				print("failed to revieve")
				return 0
			return 1
		except:
			print("PM not found")
			return 0
	
	def start_3(self):
		try:
			sync = bytes([255])
			self.ser.write(sync)
			code = bytes([3])
			self.ser.write(code)
			for i in range(0,24):
				buff = bytes([0])
				self.ser.write(buff)
			return 1
		except:
			print("PM not found")
			return 0

	def get_graph(self):

		data = [[],[]]
		atr = []
		vent_d = []
		ECG_value = [0,0,0,0]
		packets_to_read = 2
		for n in range(packets_to_read):
			time.sleep(0.4) 
			bytesToRead = self.ser.in_waiting

			readData = False
			for i in range(bytesToRead):
				if (self.ser.read() == bytes([255]) and self.ser.read() == bytes([3])):
					readData = True
					bytesToRead = self.ser.in_waiting
					break
			
			if(not readData): #No data received
				atr=atr+[0]*3
				vent_d=vent_d+[0]*3
			else: #Data is received
				for i in range(6):

					bytesToRead = self.ser.in_waiting
					if (bytesToRead >= 4):
						ECG_value[0] = self.ser.read()
						ECG_value[1] = self.ser.read()
						ECG_value[2] = self.ser.read()
						ECG_value[3] = self.ser.read()
						omg = ECG_value[0]+ECG_value[1]+ECG_value[2]+ECG_value[3]
						x = struct.unpack('<f', omg)
						x = x[0]
						(atr if (i%2 == 0) else vent_d).append(x)
					else:
						(atr if (i%2 == 0) else vent_d).append(float(0))
			data[0]= data[0] +atr
			data[1]= data[1] +vent_d
		# print("Data from get_graph: [AA, VA]: ",data)
		return data

	def stop_graph(self):
		try:
			sync = bytes([255])
			self.ser.write(sync)
			code = bytes([4])
			self.ser.write(code)
			for i in range(0,24):
				buff = bytes([0])
				self.ser.write(buff)
		except:
			print("PM not found")

	def clear_buff(self):
		try:
			self.ser.reset_output_buffer()
			self.ser.reset_input_buffer()
		except:
			print("PM not found")
