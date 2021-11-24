import serial 
import struct 
from PyQt5.QtCore import pyqtSignal, QThread

class serialThreadClass(QThread):
	
	def __init__(self):
		super(serialThreadClass, self).__init__()
		self.ser = serial.Serial()
		self.ser.baudrate = 115200
		self.ser.port = "COM8"
		self.ser.timeout = 3

	def open_serial(self):
		self.ser.open()
		if(self.ser.isOpen()):
			print("Opened: "+ self.ser.port)

	def close_serial(self):
		self.ser.close()
		print("Closed: "+ self.ser.port)

	def check_conn(self):
		sync = bytes([255])
		self.ser.write(sync)
		echo = bytes([1])
		self.ser.write(echo)
		for i in range(0,30):
			buff = bytes([0])
			self.ser.write(buff)

		sync = self.ser.readline(1) # sync
		sync = int.from_bytes(sync,'little')
		if(sync == 255):
			return 1
		else:
			print("Sync. Failure")
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
				# have a check tolernce function? here is where we'd change/ round the parameters 
				return temp

			else:
				print("Func. Failure")
				return 0
		else:
			print("Sync. Failure")
			return 0

	def send_data(self,param_list): 
		sync = bytes([255])
		self.ser.write(sync)
		code = bytes([2])
		self.ser.write(code)

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
		pm_data = self.get_param()
		# for loop with tolerances for example if 0.2< pm_data< 0.21 success
		# if wrong values try again 
		# round(pm_data[i],2) do this with all floats!
		# ours = 135 +- 5  
		# 130< theirs <140 



	# def get_graph(self):

	# 	# self.ser.write('1')
		# while 1: button which freezes graph, the condition is based on this 
	# 		atrial = self.ser.readline(1)
	# 		ventricle = self.ser.readline(1)


		

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
