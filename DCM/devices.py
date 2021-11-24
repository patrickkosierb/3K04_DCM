# checks the device connected
import win32com.client

class Device:
	ports = None
	def __init__(self):
		self.DeviceIDList = []
		self.ports = win32com.client.GetObject("winmgmts:")
		for usb in self.ports.InstancesOf("Win32_USBHub"):
			if (usb.Name == "J-Link driver"):
				self.DeviceIDList.append(usb.DeviceID)

	def Get_Current_ID(self):
		return self.DeviceIDList

	def Get_Past_PMs(self):
		db = open("data/pacemakers.txt","r")
		IDs = []
		Names = []
		for log in db:
			l = log.split(", ")		
			l[1]=l[1].strip()
			IDs.append(l[0])
			Names.append(l[1])
		db.close()
		return IDs, Names


	def compare_devices(self):
		current = self.Get_Current_ID()
		pastIDs = self.Get_Past_PMs()[0]
		pastNames = self.Get_Past_PMs()[1]

		for i in range(0, len(pastIDs)):
			if(current[0] == pastIDs[i]):
				return pastNames[i]
		return 0

	def add_device(self,name):
		current = self.Get_Current_ID()[0]
		db = open("data/pacemakers.txt","a")
		db.write("\n"+current+', '+name)
		db.close()

	def get_PM(self):
		return self.compare_devices()
		