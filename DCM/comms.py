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
		self.ser.timeout = 2

	def open_serial(self):
		try:
			self.ser.open()
			if(self.ser.isOpen()):
				print("Opened: "+ self.ser.port)
		except:
			print("PM NOT CON")

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
			print("pm not conn")

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
					# print(temp[i])
				# uint16
				for i in range(10,13):
					temp[i] = self.ser.readline(2)
					temp[i] = struct.unpack('<h', temp[i])
					temp[i] = str(temp[i][0])
					# print(temp[i])
				# single
				for i in range(13,15):
					temp[i] = self.ser.readline(4)
					temp[i] = struct.unpack('<f', temp[i])
					temp[i] = temp[i][0]
					# print(temp[i])
			
				for i in range(13,15):
					temp[i] = str(round(temp[i],2))
				print(temp)
				return temp
				
			else:
				print(code)
				print("ERROR: Receive Func. Error")
				return 0
		else:
			return 0

	def send_data(self,param_list):
		temp = param_list

		# self.ser.reset_output_buffer()
		try:
			sync = bytes([255])
			self.ser.write(sync)
			code = bytes([2])
			self.ser.write(code)
			# print(code)
			# uint8
			for i in range(0,10):
				temp[i] = bytes([int(temp[i])])
				# print(temp[i])
				self.ser.write(temp[i])
			# uint16
			for i in range(10,13):
				temp[i] = struct.pack('<h',int(temp[i]))
				# print([ "0x%02x" % b for b in temp[i]])
				self.ser.write(temp[i])
			# single
			for i in range(13,15):
				temp[i] = struct.pack('<f',float(temp[i]))
				# print([ "0x%02x" % b for b in temp[i]])
				self.ser.write(temp[i])
			# pm_data = self.get_param()
		
			return 1
		except:
			print("pn not con")



	def send_3(self):
		sync = bytes([255])
		self.ser.write(sync)
		code = bytes([3])
		self.ser.write(code)
		for i in range(0,24):
			buff = bytes([0])
			self.ser.write(buff)
		sync = self.ser.readline(1) # sync
		sync = int.from_bytes(sync,'little')
		if(sync == 255):
			code = self.ser.readline(1)
			code = int.from_bytes(code,'little')
			if(code == 3):
				return 1
			else:
				print("ERROR: Graphs Func. Error")
				return 0
		else:
			print("ERROR: Graphs Sync. Error")
			return 0


	def get_graph(self):
		data = []

		atrial = self.ser.readline(4)
		atrial = struct.unpack('<f', atrial)
		atrial = atrial[0]
		data.append(atrial)

		vent = self.ser.readline(4)
		vent = struct.unpack('<f', vent)
		vent = vent[0]
		data.append(vent)
		time.sleep(0.1)
		print("get graph")
		print(data)
		return data



	def stop_graph(self):
		sync = bytes([255])
		self.ser.write(sync)
		code = bytes([4])
		self.ser.write(code)
		for i in range(0,24):
			buff = bytes([0])
			self.ser.write(buff)



	# func 1 echo parameters
	# send sync
	# send 0x01 and 00000000000000000
	# read for sync
	# read for 0x02 (func 2)
	# read param

	# func 2 write parameters to pm
	# send sync
	# send 0x02 
	# send param
	# call func 1
	# compare param  
	# wrong data run func 2 again

	# func 3 command pm to send ecg data and store
	# send sync
	# send 0x03 000000000000
	# READ
	# read for sync
	# read for 0x03
	# read ecgdata (n points tbd)
	# JMP READ

	# maybe another function for 

	# func 4 stop sending ecg
    # send sync
    # send 0x04 0000000000000000000000000
