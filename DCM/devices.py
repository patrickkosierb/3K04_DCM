# checks the device connected
import win32com.client

class Device:
	ports = None
	def __init__(self):
		self.check_ports()

	def check_ports(self): #checks ports called by constructor
		self.DeviceIDList = []
		self.ports = win32com.client.GetObject("winmgmts:")
		for usb in self.ports.InstancesOf("Win32_USBHub"):
			if (usb.Name == "J-Link driver"):
				self.DeviceIDList.append(usb.DeviceID)
		if len(self.DeviceIDList) == 0:
			self.DeviceIDList.append("0")

	def Get_Current_ID(self): #gets id of pacemaker
		return self.DeviceIDList

	def Get_Past_PMs(self): #gets history of pms
		db = open("data/pacemakers.txt","r")
		IDs = []
		Names = []
		index = []
		for log in db:
			l = log.split(", ")		
			l[1]=l[1].strip()
			IDs.append(l[0])
			Names.append(l[1])
			index.append(l[2])
		
		db.close()
		return IDs, Names, index


	def compare_devices(self): #compares plugged in pm with old ones
		self.check_ports()
		current = self.Get_Current_ID()
		# print(current)
		pastIDs = self.Get_Past_PMs()[0]
		pastNames = self.Get_Past_PMs()[1]
		index = self.Get_Past_PMs()[2]
		for i in range(0, len(pastIDs)):
			if(current[0] == pastIDs[i]):
				return pastNames[i], index[i]
		return 0, 0

	def add_device(self,name): #adds new pm to text file
		current = self.Get_Current_ID()[0]
		db = open("data/pacemakers.txt","a")
		db.write("\n"+current+', '+name+', '+str(len(self.Get_Past_PMs()[0])+1))
		db.close()

	def get_PM(self): #gets valuable info on pm
		return self.compare_devices()

		