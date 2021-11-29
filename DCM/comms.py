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
		self.ser.timeout = 0.5

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
				# print(temp)
				return temp
				
			else:
				print(code)
				print("ERROR: Receive Func. Error")
				return 0
		else:
			return 0

	def send_data(self,param_list):
		temp = copy.deepcopy(param_list)

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
			time.sleep(2)
			pm_data = self.get_param()
			pm_data[13] = float(pm_data[13])
			pm_data[13]=round(pm_data[13],2)
			pm_data[14] = float(pm_data[14])
			pm_data[14]=round(pm_data[14],2)
			pm_data[13] = str(pm_data[13])
			pm_data[14] = str(pm_data[14])

			if(pm_data == param_list):
				print("successfully sent data")
				return 1
			else:
				print("failed to revieve")
				return 0
			return 1
		except:
			print("pn not con")
			return 0







	# def send_3(self):
	# 	try:
	# 		sync = bytes([255])
	# 		self.ser.write(sync)
	# 		code = bytes([3])
	# 		self.ser.write(code)
	# 		for i in range(0,24):
	# 			buff = bytes([0])
	# 			self.ser.write(buff)
	# 		sync = self.ser.readline(1) # sync
	# 		sync = int.from_bytes(sync,'little')
	# 		if(sync == 255):
	# 			code = self.ser.readline(1)
	# 			code = int.from_bytes(code,'little')
	# 			if(code == 3):
	# 				return 1
	# 			else:
	# 				print("ERROR: Graphs Func. Error")
	# 				return 0
	# 		else:
	# 			print("ERROR: Graphs Sync. Error")
	# 			return 0
	# 	except:
	# 		print("PM not found")
	# 		return 0
	
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
			print("pm not found")	
			return 0

	def read_3(self):
		try:
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
				print(sync)
				print("ERROR: Graphs Sync. Error")
				return 0	
		except:

			print("pm not found")
			return 0	

	def get_graph(self):

		data = []
		atr = []
		vent_d = []

		for i in range(0, 9):
			if(i==3 or i == 6):
				self.read_3()
			atrial = self.ser.readline(4)
			atrial = struct.unpack('<f', atrial)
			# print(atrial)
			atrial = atrial[0]
			atr.append(atrial)
			
			vent = self.ser.readline(4)
			vent = struct.unpack('<f', vent)
			# print(vent)
			vent = vent[0]
			vent_d.append(vent)
		# for i in range(0, 3):


		# 	atrial = self.ser.readline(4)
		# 	atrial = struct.unpack('<f', atrial)
		# 	# print(atrial)
		# 	atrial = atrial[0]
		# 	atr.append(atrial)
			
		# 	vent = self.ser.readline(4)
		# 	vent = struct.unpack('<f', vent)
		# 	# print(vent)
		# 	vent = vent[0]
		# 	vent_d.append(vent)

		data.append(atr)
		data.append(vent_d)
		print("Data from get_graph: [AA, VA]: ",data)
		return data
		# else:
			# return 

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
			print("pm not found")

	def clear_buff(self):
		try:
			self.ser.reset_output_buffer()
			self.ser.reset_input_buffer()
		except:
			print("Pm not found")
