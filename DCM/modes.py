# @ file: mode.py
# @ brief: mode file contains all mode classes (AOO AAI VOO VII)

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget, QInputDialog

import sys
import sqlite3
import os
import string
import numpy as np

import config
import menu
import welcome
import account
from helpers import go_to_page, update_current, clear_box, load_current, update_text, isDigit

import copy
import comms
import devices
import time

last_param = ['0', '0', '0', '0','0', '0', '0','0', '0', '0', '0','0', '0', '0', '0']
config.current_pm("000")

myDevice = devices.Device()
mySerial = comms.serialThreadClass()

status = 0

class mode(QDialog):
	def __init__(self):
		# get param list from_serial(param)
		super(mode, self).__init__()
		loadUi("interface/mode.ui", self)

		mySerial.open_serial()
		recieved = mySerial.get_param()
		mySerial.close_serial()
		
		if(recieved):
			global status 
			status = 1
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.user_display.setText("User: "+config.is_current_user())
			self.update_patient()
			update_text(recieved)
		else:
			status = 0
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")

		self.access.clicked.connect(self.mode_check)
		self.user_display.setText("User: "+config.is_current_user())
		self.logout.clicked.connect(self.go_to_logout)
		self.account.clicked.connect(self.go_to_account)
		self.Back.clicked.connect(self.go_to_menu)

	def mode_check(self):
		last_param = load_current()
		if(last_param[0] == '1'):
			aoo = aoo_mode()
			go_to_page(aoo)		
		elif(last_param[0] == '2'):
			aai = aai_mode()
			go_to_page(aai)			
		elif(last_param[0] == '3'):
			aoor = aoor_mode()
			go_to_page(aoor)		
		elif(last_param[0] == '4'):
			aair = aair_mode()
			go_to_page(aair)
		elif(last_param[0] == '5'):
			voo = voo_mode()
			go_to_page(voo)
		elif(last_param[0] == '6'):
			vvi = vvi_mode()
			go_to_page(vvi)
		elif(last_param[0] == '7'):
			voor = voor_mode()
			go_to_page(voor)
		elif(last_param[0] == '8'):
			vvir = vvir_mode()
			go_to_page(vvir)
		elif(last_param[0] == '9'):
			door = door_mode()
			go_to_page(door)
		elif(last_param[0] == '10'):
			doo = doo_mode()
			go_to_page(doo)
		else:
			no = no_pace()
			go_to_page(no)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	def go_to_account(self):
		account_var = account.account_page()
		go_to_page(account_var)

	def update_patient(self):
		if(myDevice.get_PM()[0]==0):
			print("Not a past device.")
			text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
			if(result == True):
				myDevice.add_device(str(text))
				cur = myDevice.get_PM()
				self.pacemaker_number.setText("Patient: "+cur[0])
				config.current_pm(cur[1])
		else:
			cur = myDevice.get_PM()
			self.pacemaker_number.setText("Patient: "+cur[0])
			config.current_pm(cur[1])


# no pacing

class no_pace(QDialog):
	def __init__(self):
		# get param list from_serial(param)
		super(no_pace, self).__init__()
		loadUi("interface/no_mode.ui", self)
		if(status):
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.update_patient()
		else:
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")
		self.user_display.setText("User: "+config.is_current_user())
		self.logout.clicked.connect(self.go_to_logout)
		self.account.clicked.connect(self.go_to_account)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.aoor.clicked.connect(self.go_to_aoor)
		self.aair.clicked.connect(self.go_to_aair)
		self.voor.clicked.connect(self.go_to_voor)
		self.vvir.clicked.connect(self.go_to_vvir)
		self.doo.clicked.connect(self.go_to_doo)
		self.door.clicked.connect(self.go_to_door)
		self.Back.clicked.connect(self.go_to_menu)
		self.stop.clicked.connect(self.send_to_pm)


	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)

	def go_to_aoor(self): 
		aoor = aoor_mode()
		go_to_page(aoor)

	def go_to_aair(self): 
		aair = aair_mode()
		go_to_page(aair)

	def go_to_voor(self): 
		voor = voor_mode()
		go_to_page(voor)

	def go_to_vvir(self): 
		vvir = vvir_mode()
		go_to_page(vvir)

	def go_to_doo(self): 
		doo = doo_mode()
		go_to_page(doo)

	def go_to_door(self): 
		door = door_mode()
		go_to_page(door)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	def go_to_account(self):
		account_var = account.account_page()
		go_to_page(account_var)

	def update_patient(self):
		if(myDevice.get_PM()[0]==0):
			print("not a past device")
			text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
			if(result == True):
				myDevice.add_device(str(text))
				cur = myDevice.get_PM()
				self.pacemaker_number.setText("Patient: "+cur[0])
				config.current_pm(cur[1])
		else:
			cur = myDevice.get_PM()
			self.pacemaker_number.setText("Patient: "+cur[0])
			config.current_pm(cur[1])

	#take current and update text file
	def send_to_pm(self):
		last_param = load_current()
		last_param[0] = '0'
		temp = copy.deepcopy(last_param)
		mySerial.open_serial()	
		send = mySerial.send_data(temp)
		mySerial.close_serial()
		if(send):
			self.update_patient()
			update_text(last_param)
			global status
			status = 1
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.conn_error.setText("")
			print(last_param)	
		else:
			status = 0
			self.conn_error.setText("Check Connection")
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")


	def get_from_pm(self):
		mySerial.open_serial()
		recieved = mySerial.get_param()
		mySerial.close_serial()
		if(recieved):
			global status
			status = 1
			self.update_patient()
			update_text(recieved)
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.conn_error.setText("")

		else:
			status = 0
			self.conn_error.setText("Check Connection")
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")


# ATRIAL
class aoo_mode(QDialog):
	def __init__(self):
		# get param list from_serial(param)
		super(aoo_mode, self).__init__()
		loadUi("interface/aoo_mode.ui", self)
		if(status):
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.update_patient()
		else:
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")
		self.current_param()
		self.logout.clicked.connect(self.go_to_logout)
		self.account.clicked.connect(self.go_to_account)
		self.no_pacing.clicked.connect(self.go_to_no)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.aoor.clicked.connect(self.go_to_aoor)
		self.aair.clicked.connect(self.go_to_aair)
		self.voor.clicked.connect(self.go_to_voor)
		self.vvir.clicked.connect(self.go_to_vvir)
		self.doo.clicked.connect(self.go_to_doo)
		self.door.clicked.connect(self.go_to_door)
		self.Back.clicked.connect(self.go_to_menu)
		
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.current_param) #current_param
		self.clear.clicked.connect(self.clear_inputs)
		self.update_pm.clicked.connect(self.send_to_pm)
		self.refresh.clicked.connect(self.get_from_pm)
	
	def mode_check(self):
		last_param = load_current()
		if(last_param[0] == '1'):
			aoo = aoo_mode()
			go_to_page(aoo)		
		elif(last_param[0] == '2'):
			aai = aai_mode()
			go_to_page(aai)			
		elif(last_param[0] == '3'):
			aoor = aoor_mode()
			go_to_page(aoor)		
		elif(last_param[0] == '4'):
			aair = aair_mode()
			go_to_page(aair)
		elif(last_param[0] == '5'):
			voo = voo_mode()
			go_to_page(voo)
		elif(last_param[0] == '6'):
			vvi = vvi_mode()
			go_to_page(vvi)
		elif(last_param[0] == '7'):
			voor = voor_mode()
			go_to_page(voor)
		elif(last_param[0] == '8'):
			vvir = vvir_mode()
			go_to_page(vvir)
		elif(last_param[0] == '9'):
			door = door_mode()
			go_to_page(door)
		elif(last_param[0] == '10'):
			doo = doo_mode()
			go_to_page(doo)
		else:
			no = no_pace()
			go_to_page(no)

	def go_to_no(self): 
		no = no_pace()
		go_to_page(no)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)

	def go_to_aoor(self): 
		aoor = aoor_mode()
		go_to_page(aoor)

	def go_to_aair(self): 
		aair = aair_mode()
		go_to_page(aair)

	def go_to_voor(self): 
		voor = voor_mode()
		go_to_page(voor)

	def go_to_vvir(self): 
		vvir = vvir_mode()
		go_to_page(vvir)

	def go_to_doo(self): 
		doo = doo_mode()
		go_to_page(doo)

	def go_to_door(self): 
		door = door_mode()
		go_to_page(door)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	def go_to_account(self):
		account_var = account.account_page()
		go_to_page(account_var)

	# uses file io functions to take CURRENT parameters TAKEN FROM PACEMAKER and load them into the text boxes
	def current_param(self):
		self.user_display.setText("User: "+config.is_current_user())
		last_param = load_current()
		self.LRL_Current.setText(last_param[1]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(last_param[2])
		self.AA_Current.setText(last_param[13])
		self.APW_Current.setText(last_param[8])

	# update the current parameters, apply changes is only for ui, send to pacemaker will actually update pacemaker
	def update_param(self):
		# check here?
		# x = str(self.LRL.currentText())
		# x2 = self.LRL_Current.text()
		# y2 = self.URL_Current.text()
		# y = str(self.URL.currentText())
		# if(isDigit(x) == True):
		# 	x = int(x)
		# 	if(x>int(y2)):
		# 		print("error1")
		# 		self.LRL.setCurrentIndex(0)
		# if(isDigit(y) == True):
		# 	y = int(y)
		# 	if(y<int(x2)):
		# 		print("error2")
		# 		self.URL.setCurrentIndex(0)

		User = [self.LRL.currentText(), self.URL.currentText(),self.AA.currentText(),self.APW.currentText()];
		Current = [self.LRL_Current, self.URL_Current,self.AA_Current,self.APW_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4]
		update_current(User, Current, Label)

	def clear_inputs(self):
		User = [self.LRL, self.URL,self.AA,self.APW];
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4]
		clear_box(User,Label)

	def update_patient(self):
		if(myDevice.get_PM()[0]==0):
			print("not a past device")
			text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
			if(result == True):
				myDevice.add_device(str(text))
				cur = myDevice.get_PM()
				self.pacemaker_number.setText("Patient: "+cur[0])
				config.current_pm(cur[1])
		else:
			cur = myDevice.get_PM()
			self.pacemaker_number.setText("Patient: "+cur[0])
			config.current_pm(cur[1])

	#take current and update text file
	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_5.setText("")
			last_param = load_current()
			last_param[0] = '1'
			last_param[1] = self.LRL_Current.text()
			last_param[2] = self.URL_Current.text()
			last_param[13] = self.AA_Current.text()
			last_param[8] = self.APW_Current.text()
			temp = copy.deepcopy(last_param)
			mySerial.open_serial()	
			send = mySerial.send_data(temp)
			mySerial.close_serial()
			if(send):
				self.clear_inputs()
				self.update_patient()
				update_text(last_param)
				global status
				status = 1
				self.connected.setText("Connected")
				self.disconnected.setText("")
				self.conn_error.setText("")
				print(last_param)	
			else:
				status = 0
				self.conn_error.setText("Check Connection")
				self.disconnected.setText("Disconnected")
				self.connected.setText("")
				self.pacemaker_number.setText("")
		else:
			self.INVALID_5.setText("*Please confirm changes")

	def get_from_pm(self):
		mySerial.open_serial()
		recieved = mySerial.get_param()
		mySerial.close_serial()
		if(recieved):
			global status
			status = 1
			self.update_patient()
			update_text(recieved)
			self.mode_check()
			self.current_param()
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.conn_error.setText("")
			self.clear_inputs()
		else:
			status = 0
			self.conn_error.setText("Check Connection")
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")

	
class aai_mode(QDialog):
	def __init__(self):
		super(aai_mode, self).__init__()
		loadUi("interface/aai_mode.ui", self)
		if(status):
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.update_patient()
		else:
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")
		self.current_param()
		self.logout.clicked.connect(self.go_to_logout)
		self.account.clicked.connect(self.go_to_account)
		self.no_pacing.clicked.connect(self.go_to_no)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.aoor.clicked.connect(self.go_to_aoor)
		self.aair.clicked.connect(self.go_to_aair)
		self.voor.clicked.connect(self.go_to_voor)
		self.vvir.clicked.connect(self.go_to_vvir)
		self.doo.clicked.connect(self.go_to_doo)
		self.door.clicked.connect(self.go_to_door)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.current_param)
		self.update_pm.clicked.connect(self.send_to_pm)
		self.clear.clicked.connect(self.clear_inputs)
		self.refresh.clicked.connect(self.get_from_pm)

	def mode_check(self):
		last_param = load_current()
		if(last_param[0] == '1'):
			aoo = aoo_mode()
			go_to_page(aoo)		
		elif(last_param[0] == '2'):
			aai = aai_mode()
			go_to_page(aai)			
		elif(last_param[0] == '3'):
			aoor = aoor_mode()
			go_to_page(aoor)		
		elif(last_param[0] == '4'):
			aair = aair_mode()
			go_to_page(aair)
		elif(last_param[0] == '5'):
			voo = voo_mode()
			go_to_page(voo)
		elif(last_param[0] == '6'):
			vvi = vvi_mode()
			go_to_page(vvi)
		elif(last_param[0] == '7'):
			voor = voor_mode()
			go_to_page(voor)
		elif(last_param[0] == '8'):
			vvir = vvir_mode()
			go_to_page(vvir)
		elif(last_param[0] == '9'):
			door = door_mode()
			go_to_page(door)
		elif(last_param[0] == '10'):
			doo = doo_mode()
			go_to_page(doo)
		else:
			no = no_pace()
			go_to_page(no)

	def go_to_no(self): 
		no = no_pace()
		go_to_page(no)
	
	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)

	def go_to_aoor(self): 
		aoor = aoor_mode()
		go_to_page(aoor)

	def go_to_aair(self): 
		aair = aair_mode()
		go_to_page(aair)

	def go_to_voor(self): 
		voor = voor_mode()
		go_to_page(voor)

	def go_to_vvir(self): 
		vvir = vvir_mode()
		go_to_page(vvir)

	def go_to_doo(self): 
		doo = doo_mode()
		go_to_page(doo)

	def go_to_door(self): 
		door = door_mode()
		go_to_page(door)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	def go_to_account(self):
		account_var = account.account_page()
		go_to_page(account_var)

	def current_param(self):
		self.user_display.setText("User: "+config.is_current_user())
		last_param = load_current()
		self.LRL_Current.setText(last_param[1]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(last_param[2])
		self.AA_Current.setText(last_param[13])
		self.APW_Current.setText(last_param[8])
		self.ARP_Current.setText(last_param[10])
	
	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.AA.currentText(),self.APW.currentText(),self.ARP.currentText()]
		Current = [self.LRL_Current, self.URL_Current,self.AA_Current,self.APW_Current,self.ARP_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5]
		update_current(User, Current, Label)
	
	def clear_inputs(self):
		User = [self.LRL, self.URL,self.AA,self.APW,self.ARP]
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5]
		clear_box(User,Label)

	def update_patient(self):
		if(myDevice.get_PM()[0]==0):
			print("not a past device")
			text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
			if(result == True):
				myDevice.add_device(str(text))
				cur = myDevice.get_PM()
				self.pacemaker_number.setText("Patient: "+cur[0])
				config.current_pm(cur[1])
		else:
			cur = myDevice.get_PM()
			self.pacemaker_number.setText("Patient: "+cur[0])
			config.current_pm(cur[1])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_5.setText("")
			last_param = load_current()
			last_param[0] = '2'
			last_param[1] = self.LRL_Current.text()
			last_param[2] = self.URL_Current.text()
			last_param[13] = self.AA_Current.text()
			last_param[8] = self.APW_Current.text()
			last_param[10] = self.ARP_Current.text()
			temp = copy.deepcopy(last_param)
			mySerial.open_serial()	
			send = mySerial.send_data(temp)
			mySerial.close_serial()
			if(send):
				self.clear_inputs()
				self.update_patient()
				update_text(last_param)
				global status
				status = 1
				self.connected.setText("Connected")
				self.disconnected.setText("")
				self.conn_error.setText("")
				print(last_param)	
			else:
				status = 0
				self.conn_error.setText("Check Connection")
				self.disconnected.setText("Disconnected")
				self.connected.setText("")
				self.pacemaker_number.setText("")
		else:
			self.INVALID_5.setText("*Please confirm changes")
	
	def get_from_pm(self):
		mySerial.open_serial()
		recieved = mySerial.get_param()
		mySerial.close_serial()
		if(recieved):
			global status
			status = 1
			self.update_patient()
			update_text(recieved)
			self.mode_check()
			self.current_param()
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.conn_error.setText("")
			self.clear_inputs()
		else:
			status = 0
			self.conn_error.setText("Check Connection")
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")
# VENTRICLE 

class voo_mode(QDialog):
	def __init__(self):
		super(voo_mode, self).__init__()
		loadUi("interface/voo_mode.ui", self)

		if(status):
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.update_patient()
		else:
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")
		self.current_param()
		self.update_pm.clicked.connect(self.send_to_pm)
		self.refresh.clicked.connect(self.get_from_pm)
		self.logout.clicked.connect(self.go_to_logout)
		self.account.clicked.connect(self.go_to_account)
		self.no_pacing.clicked.connect(self.go_to_no)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.aoor.clicked.connect(self.go_to_aoor)
		self.aair.clicked.connect(self.go_to_aair)
		self.voor.clicked.connect(self.go_to_voor)
		self.vvir.clicked.connect(self.go_to_vvir)
		self.doo.clicked.connect(self.go_to_doo)
		self.door.clicked.connect(self.go_to_door)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.current_param)
		self.clear.clicked.connect(self.clear_inputs)

	def mode_check(self):
		last_param = load_current()
		if(last_param[0] == '1'):
			aoo = aoo_mode()
			go_to_page(aoo)		
		elif(last_param[0] == '2'):
			aai = aai_mode()
			go_to_page(aai)			
		elif(last_param[0] == '3'):
			aoor = aoor_mode()
			go_to_page(aoor)		
		elif(last_param[0] == '4'):
			aair = aair_mode()
			go_to_page(aair)
		elif(last_param[0] == '5'):
			voo = voo_mode()
			go_to_page(voo)
		elif(last_param[0] == '6'):
			vvi = vvi_mode()
			go_to_page(vvi)
		elif(last_param[0] == '7'):
			voor = voor_mode()
			go_to_page(voor)
		elif(last_param[0] == '8'):
			vvir = vvir_mode()
			go_to_page(vvir)
		elif(last_param[0] == '9'):
			door = door_mode()
			go_to_page(door)
		elif(last_param[0] == '10'):
			doo = doo_mode()
			go_to_page(doo)
		else:
			no = no_pace()
			go_to_page(no)

	def go_to_no(self): 
		no = no_pace()
		go_to_page(no)
	
	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)

	def go_to_aoor(self): 
		aoor = aoor_mode()
		go_to_page(aoor)

	def go_to_aair(self): 
		aair = aair_mode()
		go_to_page(aair)

	def go_to_voor(self): 
		voor = voor_mode()
		go_to_page(voor)

	def go_to_vvir(self): 
		vvir = vvir_mode()
		go_to_page(vvir)

	def go_to_doo(self): 
		doo = doo_mode()
		go_to_page(doo)

	def go_to_door(self): 
		door = door_mode()
		go_to_page(door)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)
	
	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)
	
	def go_to_account(self):
		account_var = account.account_page()
		go_to_page(account_var)

	def current_param(self):
		self.user_display.setText("User: "+config.is_current_user())
		# self.pacemaker_number.setText("Pacemaker ID: "+config.is_current_pm())
		last_param = load_current()
		self.LRL_Current.setText(last_param[1]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(last_param[2])
		self.VA_Current.setText(last_param[14])
		self.VPW_Current.setText(last_param[9])

	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.VA.currentText(),self.VPW.currentText()]
		Current = [self.LRL_Current, self.URL_Current,self.VA_Current,self.VPW_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4]
		update_current(User, Current, Label)

	def update_patient(self):
		if(myDevice.get_PM()[0]==0):
			print("not a past device")
			text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
			if(result == True):
				myDevice.add_device(str(text))
				cur = myDevice.get_PM()
				self.pacemaker_number.setText("Patient: "+cur[0])
				config.current_pm(cur[1])
		else:
			cur = myDevice.get_PM()
			self.pacemaker_number.setText("Patient: "+cur[0])
			config.current_pm(cur[1])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_5.setText("")
			last_param = load_current()
			last_param[0] = '5'
			last_param[1] = self.LRL_Current.text()
			last_param[2] = self.URL_Current.text()
			last_param[14] = self.VA_Current.text()
			last_param[9] = self.VPW_Current.text()
			temp = copy.deepcopy(last_param)
			mySerial.open_serial()	
			send = mySerial.send_data(temp)
			mySerial.close_serial()
			if(send):
				self.clear_inputs()
				self.update_patient()
				update_text(last_param)
				global status
				status = 1
				self.connected.setText("Connected")
				self.disconnected.setText("")
				self.conn_error.setText("")
				print(last_param)	
			else:
				status = 0
				self.conn_error.setText("Check Connection")
				self.disconnected.setText("Disconnected")
				self.connected.setText("")
				self.pacemaker_number.setText("")
		else:
			self.INVALID_5.setText("*Please confirm changes")


	def get_from_pm(self):
		mySerial.open_serial()
		recieved = mySerial.get_param()
		mySerial.close_serial()
		if(recieved):
			global status
			status = 1
			self.update_patient()
			update_text(recieved)
			self.mode_check()
			self.current_param()
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.conn_error.setText("")
			self.clear_inputs()
		else:
			status = 0
			self.conn_error.setText("Check Connection")
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")

	
	def clear_inputs(self):
		User = [self.LRL, self.URL,self.VA,self.VPW]
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4]
		clear_box(User,Label)

class vvi_mode(QDialog):
	def __init__(self):
		super(vvi_mode, self).__init__()
		loadUi("interface/vvi_mode.ui", self)
		if(status):
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.update_patient()
		else:
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")
		self.current_param()
		self.update_pm.clicked.connect(self.send_to_pm)
		self.refresh.clicked.connect(self.get_from_pm)
		self.logout.clicked.connect(self.go_to_logout)
		self.account.clicked.connect(self.go_to_account)	
		self.no_pacing.clicked.connect(self.go_to_no)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.aoor.clicked.connect(self.go_to_aoor)
		self.aair.clicked.connect(self.go_to_aair)
		self.voor.clicked.connect(self.go_to_voor)
		self.vvir.clicked.connect(self.go_to_vvir)
		self.doo.clicked.connect(self.go_to_doo)
		self.door.clicked.connect(self.go_to_door)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.current_param)
		self.clear.clicked.connect(self.clear_inputs)
	
	def mode_check(self):
		last_param = load_current()
		if(last_param[0] == '1'):
			aoo = aoo_mode()
			go_to_page(aoo)		
		elif(last_param[0] == '2'):
			aai = aai_mode()
			go_to_page(aai)			
		elif(last_param[0] == '3'):
			aoor = aoor_mode()
			go_to_page(aoor)		
		elif(last_param[0] == '4'):
			aair = aair_mode()
			go_to_page(aair)
		elif(last_param[0] == '5'):
			voo = voo_mode()
			go_to_page(voo)
		elif(last_param[0] == '6'):
			vvi = vvi_mode()
			go_to_page(vvi)
		elif(last_param[0] == '7'):
			voor = voor_mode()
			go_to_page(voor)
		elif(last_param[0] == '8'):
			vvir = vvir_mode()
			go_to_page(vvir)
		elif(last_param[0] == '9'):
			door = door_mode()
			go_to_page(door)
		elif(last_param[0] == '10'):
			doo = doo_mode()
			go_to_page(doo)
		else:
			no = no_pace()
			go_to_page(no)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)
	
	def go_to_no(self): 
		no = no_pace()
		go_to_page(no)
	
	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)	

	def go_to_aoor(self): 
		aoor = aoor_mode()
		go_to_page(aoor)

	def go_to_aair(self): 
		aair = aair_mode()
		go_to_page(aair)

	def go_to_voor(self): 
		voor = voor_mode()
		go_to_page(voor)

	def go_to_vvir(self): 
		vvir = vvir_mode()
		go_to_page(vvir)

	def go_to_doo(self): 
		doo = doo_mode()
		go_to_page(doo)

	def go_to_door(self): 
		door = door_mode()
		go_to_page(door)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_account(self):
		account_var = account.account_page()
		go_to_page(account_var)

	def current_param(self):
		self.user_display.setText("User: "+config.is_current_user())
		# self.pacemaker_number.setText("Pacemaker ID: "+config.is_current_pm())
		last_param = load_current()
		self.LRL_Current.setText(last_param[1]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(last_param[2])
		self.VA_Current.setText(last_param[14])
		self.VPW_Current.setText(last_param[9])
		self.VRP_Current.setText(last_param[11])

	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.VA.currentText(),self.VPW.currentText(),self.VRP.currentText()]
		Current = [self.LRL_Current, self.URL_Current,self.VA_Current,self.VPW_Current,self.VRP_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5]
		update_current(User, Current, Label)


	def update_patient(self):
		if(myDevice.get_PM()[0]==0):
			print("not a past device")
			text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
			if(result == True):
				myDevice.add_device(str(text))
				cur = myDevice.get_PM()
				self.pacemaker_number.setText("Patient: "+cur[0])
				config.current_pm(cur[1])
		else:
			cur = myDevice.get_PM()
			self.pacemaker_number.setText("Patient: "+cur[0])
			config.current_pm(cur[1])	

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_5.setText("")
			last_param = load_current()
			last_param[0] = '6'
			last_param[1] = self.LRL_Current.text()
			last_param[2] = self.URL_Current.text()
			last_param[14] = self.VA_Current.text()
			last_param[9] = self.VPW_Current.text()
			last_param[11] = self.VRP_Current.text()
			temp = copy.deepcopy(last_param)
			mySerial.open_serial()	
			send = mySerial.send_data(temp)
			mySerial.close_serial()
			if(send):
				self.clear_inputs()
				self.update_patient()
				update_text(last_param)
				global status
				status = 1
				self.connected.setText("Connected")
				self.disconnected.setText("")
				self.conn_error.setText("")
				print(last_param)	
			else:
				status = 0
				self.conn_error.setText("Check Connection")
				self.disconnected.setText("Disconnected")
				self.connected.setText("")
				self.pacemaker_number.setText("")
		else:
			self.INVALID_8.setText("*Please confirm changes")

	def get_from_pm(self):
		mySerial.open_serial()
		recieved = mySerial.get_param()
		mySerial.close_serial()
		if(recieved):
			global status
			status = 1
			self.update_patient()
			update_text(recieved)
			self.mode_check()
			self.current_param()
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.conn_error.setText("")
			self.clear_inputs()
		else:
			status = 0
			self.conn_error.setText("Check Connection")
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")

	def clear_inputs(self):
		User = [self.LRL, self.URL,self.VA,self.VPW,self.VRP]
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5]
		clear_box(User,Label)



# a2

class aoor_mode(QDialog):
	def __init__(self):
		# get param list from_serial(param)
		super(aoor_mode, self).__init__()
		loadUi("interface/aoor_mode.ui", self)
		if(status):
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.update_patient()
		else:
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")
		self.current_param()
		self.update_pm.clicked.connect(self.send_to_pm)
		self.refresh.clicked.connect(self.get_from_pm)
		self.logout.clicked.connect(self.go_to_logout)
		self.account.clicked.connect(self.go_to_account)
		self.no_pacing.clicked.connect(self.go_to_no)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.aair.clicked.connect(self.go_to_aair)
		self.voor.clicked.connect(self.go_to_voor)
		self.vvir.clicked.connect(self.go_to_vvir)
		self.doo.clicked.connect(self.go_to_doo)
		self.door.clicked.connect(self.go_to_door)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.current_param) 
		self.clear.clicked.connect(self.clear_inputs)

	def mode_check(self):
		last_param = load_current()
		if(last_param[0] == '1'):
			aoo = aoo_mode()
			go_to_page(aoo)		
		elif(last_param[0] == '2'):
			aai = aai_mode()
			go_to_page(aai)			
		elif(last_param[0] == '3'):
			aoor = aoor_mode()
			go_to_page(aoor)		
		elif(last_param[0] == '4'):
			aair = aair_mode()
			go_to_page(aair)
		elif(last_param[0] == '5'):
			voo = voo_mode()
			go_to_page(voo)
		elif(last_param[0] == '6'):
			vvi = vvi_mode()
			go_to_page(vvi)
		elif(last_param[0] == '7'):
			voor = voor_mode()
			go_to_page(voor)
		elif(last_param[0] == '8'):
			vvir = vvir_mode()
			go_to_page(vvir)
		elif(last_param[0] == '9'):
			door = door_mode()
			go_to_page(door)
		elif(last_param[0] == '10'):
			doo = doo_mode()
			go_to_page(doo)
		else:
			no = no_pace()
			go_to_page(no)

	def go_to_no(self): 
		no = no_pace()
		go_to_page(no)

	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)	

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)			

	def go_to_aair(self): 
		aair = aair_mode()
		go_to_page(aair)

	def go_to_voor(self): 
		voor = voor_mode()
		go_to_page(voor)

	def go_to_vvir(self): 
		vvir = vvir_mode()
		go_to_page(vvir)

	def go_to_doo(self): 
		doo = doo_mode()
		go_to_page(doo)

	def go_to_door(self): 
		door = door_mode()
		go_to_page(door)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	def go_to_account(self):
		account_var = account.account_page()
		go_to_page(account_var)


	def current_param(self):
		self.user_display.setText("User: "+config.is_current_user())
		# self.pacemaker_number.setText("Pacemaker ID: "+config.is_current_pm())
		last_param = load_current()
		self.LRL_Current.setText(last_param[1]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(last_param[2])
		self.AA_Current.setText(last_param[13])
		self.APW_Current.setText(last_param[8])
		self.MSR_Current.setText(last_param[3])
		self.AT_Current.setText(last_param[4])
		self.RT_Current.setText(last_param[5])
		self.RF_Current.setText(last_param[6])
		self.RCT_Current.setText(last_param[7])

	
	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.AA.currentText(),self.APW.currentText(),self.MSR.currentText(),self.AT.currentText(),self.RT.currentText(),self.RF.currentText(),self.RCT.currentText()]
		Current = [self.LRL_Current, self.URL_Current,self.AA_Current,self.APW_Current, self.MSR_Current, self.AT_Current, self.RT_Current, self.RF_Current, self.RCT_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5, self.INVALID_6, self.INVALID_9,self.INVALID_10,self.INVALID_11]
		update_current(User, Current, Label)

	def update_patient(self):
		if(myDevice.get_PM()[0]==0):
			print("not a past device")
			text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
			if(result == True):
				myDevice.add_device(str(text))
				cur = myDevice.get_PM()
				self.pacemaker_number.setText("Patient: "+cur[0])
				config.current_pm(cur[1])
		else:
			cur = myDevice.get_PM()
			self.pacemaker_number.setText("Patient: "+cur[0])
			config.current_pm(cur[1])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_8.setText("")
			last_param = load_current()
			last_param[0] = '3'
			last_param[1] = self.LRL_Current.text()
			last_param[2] = self.URL_Current.text()
			last_param[13] = self.AA_Current.text()
			last_param[8] = self.APW_Current.text()
			last_param[3] = self.MSR_Current.text()
			last_param[4] = self.AT_Current.text()
			last_param[5] = self.RT_Current.text()
			last_param[6] = self.RF_Current.text()
			last_param[7] = self.RCT_Current.text()
			temp = copy.deepcopy(last_param)
			mySerial.open_serial()	
			send = mySerial.send_data(temp)
			mySerial.close_serial()
			if(send):
				self.clear_inputs()
				self.update_patient()
				update_text(last_param)
				global status
				status = 1
				self.connected.setText("Connected")
				self.disconnected.setText("")
				self.conn_error.setText("")
				print(last_param)	
			else:
				status = 0
				self.conn_error.setText("Check Connection")
				self.disconnected.setText("Disconnected")
				self.connected.setText("")
				self.pacemaker_number.setText("")
		else:
			self.INVALID_8.setText("*Please confirm changes")

	def get_from_pm(self):
		mySerial.open_serial()
		recieved = mySerial.get_param()
		mySerial.close_serial()
		if(recieved):
			global status
			status = 1
			self.update_patient()
			update_text(recieved)
			self.mode_check()
			self.current_param()
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.conn_error.setText("")
			self.clear_inputs()
		else:
			status = 0
			self.conn_error.setText("Check Connection")
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")

	def clear_inputs(self):
		User = [self.LRL, self.URL,self.AA,self.APW,self.MSR,self.AT,self.RT,self.RF,self.RCT]
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5, self.INVALID_6, self.INVALID_9,self.INVALID_10,self.INVALID_11]
		clear_box(User,Label)



class aair_mode(QDialog):
	def __init__(self):
		# get param list from_serial(param)
		super(aair_mode, self).__init__()
		loadUi("interface/aair_mode.ui", self)
		if(status):
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.update_patient()
		else:
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")
		self.current_param()
		self.update_pm.clicked.connect(self.send_to_pm)
		self.refresh.clicked.connect(self.get_from_pm)
		self.logout.clicked.connect(self.go_to_logout)
		self.account.clicked.connect(self.go_to_account)
		self.no_pacing.clicked.connect(self.go_to_no)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.aoor.clicked.connect(self.go_to_aoor)
		self.voor.clicked.connect(self.go_to_voor)
		self.vvir.clicked.connect(self.go_to_vvir)
		self.doo.clicked.connect(self.go_to_doo)
		self.door.clicked.connect(self.go_to_door)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.current_param) 
		self.clear.clicked.connect(self.clear_inputs)

	def mode_check(self):
		last_param = load_current()
		if(last_param[0] == '1'):
			aoo = aoo_mode()
			go_to_page(aoo)		
		elif(last_param[0] == '2'):
			aai = aai_mode()
			go_to_page(aai)			
		elif(last_param[0] == '3'):
			aoor = aoor_mode()
			go_to_page(aoor)		
		elif(last_param[0] == '4'):
			aair = aair_mode()
			go_to_page(aair)
		elif(last_param[0] == '5'):
			voo = voo_mode()
			go_to_page(voo)
		elif(last_param[0] == '6'):
			vvi = vvi_mode()
			go_to_page(vvi)
		elif(last_param[0] == '7'):
			voor = voor_mode()
			go_to_page(voor)
		elif(last_param[0] == '8'):
			vvir = vvir_mode()
			go_to_page(vvir)
		elif(last_param[0] == '9'):
			door = door_mode()
			go_to_page(door)
		elif(last_param[0] == '10'):
			doo = doo_mode()
			go_to_page(doo)
		else:
			no = no_pace()
			go_to_page(no)


	def go_to_no(self): 
		no = no_pace()
		go_to_page(no)
	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)	

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)			

	def go_to_aoor(self): 
		aoor = aoor_mode()
		go_to_page(aoor)

	def go_to_voor(self): 
		voor = voor_mode()
		go_to_page(voor)

	def go_to_vvir(self): 
		vvir = vvir_mode()
		go_to_page(vvir)

	def go_to_doo(self): 
		doo = doo_mode()
		go_to_page(doo)

	def go_to_door(self): 
		door = door_mode()
		go_to_page(door)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	def go_to_account(self):
		account_var = account.account_page()
		go_to_page(account_var)

	def current_param(self):
		self.user_display.setText("User: "+config.is_current_user())
		# self.pacemaker_number.setText("Pacemaker ID: "+config.is_current_pm())
		last_param = load_current()
		self.LRL_Current.setText(last_param[1]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(last_param[2])
		self.AA_Current.setText(last_param[13])
		self.APW_Current.setText(last_param[8])
		self.ARP_Current.setText(last_param[10])
		self.MSR_Current.setText(last_param[3])
		self.AT_Current.setText(last_param[4])
		self.RT_Current.setText(last_param[5])
		self.RF_Current.setText(last_param[6])
		self.RCT_Current.setText(last_param[7])

	
	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.AA.currentText(),self.APW.currentText(),self.MSR.currentText(),self.AT.currentText(),self.RT.currentText(),self.RF.currentText(),self.RCT.currentText(),self.ARP.currentText()]
		Current = [self.LRL_Current, self.URL_Current,self.AA_Current,self.APW_Current, self.MSR_Current, self.AT_Current, self.RT_Current, self.RF_Current, self.RCT_Current, self.ARP_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5, self.INVALID_6, self.INVALID_7,self.INVALID_9,self.INVALID_10,self.INVALID_11]
		update_current(User, Current, Label)

	def update_patient(self):
		if(myDevice.get_PM()[0]==0):
			print("not a past device")
			text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
			if(result == True):
				myDevice.add_device(str(text))
				cur = myDevice.get_PM()
				self.pacemaker_number.setText("Patient: "+cur[0])
				config.current_pm(cur[1])
		else:
			cur = myDevice.get_PM()
			self.pacemaker_number.setText("Patient: "+cur[0])
			config.current_pm(cur[1])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_8.setText("")
			last_param = load_current()
			last_param[0] = '4'
			last_param[1] = self.LRL_Current.text()
			last_param[2] = self.URL_Current.text()
			last_param[13] = self.AA_Current.text()
			last_param[8] = self.APW_Current.text()
			last_param[10] = self.ARP_Current.text()
			last_param[3] = self.MSR_Current.text()
			last_param[4] = self.AT_Current.text()
			last_param[5] = self.RT_Current.text()
			last_param[6] = self.RF_Current.text()
			last_param[7] = self.RCT_Current.text()
			temp = copy.deepcopy(last_param)
			mySerial.open_serial()	
			send = mySerial.send_data(temp)
			mySerial.close_serial()
			if(send):
				self.clear_inputs()
				self.update_patient()
				update_text(last_param)
				global status
				status = 1
				self.connected.setText("Connected")
				self.disconnected.setText("")
				self.conn_error.setText("")
				print(last_param)	
			else:
				status = 0
				self.conn_error.setText("Check Connection")
				self.disconnected.setText("Disconnected")
				self.connected.setText("")
				self.pacemaker_number.setText("")
		else:
			self.INVALID_8.setText("*Please confirm changes")

	def get_from_pm(self):
		mySerial.open_serial()
		recieved = mySerial.get_param()
		mySerial.close_serial()
		if(recieved):
			global status
			status = 1
			self.update_patient()
			update_text(recieved)
			self.mode_check()
			self.current_param()
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.conn_error.setText("")
			self.clear_inputs()
		else:
			status = 0
			self.conn_error.setText("Check Connection")
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")

	def clear_inputs(self):
		User = [self.LRL, self.URL,self.AA,self.APW,self.MSR,self.AT,self.RT,self.RF,self.RCT,self.ARP]
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5, self.INVALID_6, self.INVALID_7,self.INVALID_9,self.INVALID_10,self.INVALID_11]
		clear_box(User,Label)



class voor_mode(QDialog):
	def __init__(self):
		# get param list from_serial(param)
		super(voor_mode, self).__init__()
		loadUi("interface/voor_mode.ui", self)
		if(status):
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.update_patient()
		else:
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")
		self.current_param()
		self.update_pm.clicked.connect(self.send_to_pm)
		self.refresh.clicked.connect(self.get_from_pm)
		self.logout.clicked.connect(self.go_to_logout)
		self.account.clicked.connect(self.go_to_account)
		self.no_pacing.clicked.connect(self.go_to_no)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.aoor.clicked.connect(self.go_to_aoor)
		self.aair.clicked.connect(self.go_to_aair)
		self.vvir.clicked.connect(self.go_to_vvir)
		self.doo.clicked.connect(self.go_to_doo)
		self.door.clicked.connect(self.go_to_door)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.current_param) 
		self.clear.clicked.connect(self.clear_inputs)
	
	def mode_check(self):
		last_param = load_current()
		if(last_param[0] == '1'):
			aoo = aoo_mode()
			go_to_page(aoo)		
		elif(last_param[0] == '2'):
			aai = aai_mode()
			go_to_page(aai)			
		elif(last_param[0] == '3'):
			aoor = aoor_mode()
			go_to_page(aoor)		
		elif(last_param[0] == '4'):
			aair = aair_mode()
			go_to_page(aair)
		elif(last_param[0] == '5'):
			voo = voo_mode()
			go_to_page(voo)
		elif(last_param[0] == '6'):
			vvi = vvi_mode()
			go_to_page(vvi)
		elif(last_param[0] == '7'):
			voor = voor_mode()
			go_to_page(voor)
		elif(last_param[0] == '8'):
			vvir = vvir_mode()
			go_to_page(vvir)
		elif(last_param[0] == '9'):
			door = door_mode()
			go_to_page(door)
		elif(last_param[0] == '10'):
			doo = doo_mode()
			go_to_page(doo)
		else:
			no = no_pace()
			go_to_page(no)


	def go_to_no(self): 
		no = no_pace()
		go_to_page(no)
	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)	

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)			

	def go_to_aoor(self): 
		aoor = aoor_mode()
		go_to_page(aoor)

	def go_to_aair(self): 
		aair = aair_mode()
		go_to_page(aair)

	def go_to_vvir(self): 
		vvir = vvir_mode()
		go_to_page(vvir)

	def go_to_doo(self): 
		doo = doo_mode()
		go_to_page(doo)

	def go_to_door(self): 
		door = door_mode()
		go_to_page(door)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	def go_to_account(self):
		account_var = account.account_page()
		go_to_page(account_var)

	def current_param(self):
		self.user_display.setText("User: "+config.is_current_user())
		# self.pacemaker_number.setText("Pacemaker ID: "+config.is_current_pm())
		last_param = load_current()
		self.LRL_Current.setText(last_param[1]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(last_param[2])
		self.VA_Current.setText(last_param[14])
		self.VPW_Current.setText(last_param[9])
		self.MSR_Current.setText(last_param[3])
		self.AT_Current.setText(last_param[4])
		self.RT_Current.setText(last_param[5])
		self.RF_Current.setText(last_param[6])
		self.RCT_Current.setText(last_param[7])

	
	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.VA.currentText(),self.VPW.currentText(),self.MSR.currentText(),self.AT.currentText(),self.RT.currentText(),self.RF.currentText(),self.RCT.currentText()]
		Current = [self.LRL_Current, self.URL_Current,self.VA_Current,self.VPW_Current, self.MSR_Current, self.AT_Current, self.RT_Current, self.RF_Current, self.RCT_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5, self.INVALID_6, self.INVALID_9,self.INVALID_10,self.INVALID_11]
		update_current(User, Current, Label)


	def update_patient(self):
		if(myDevice.get_PM()[0]==0):
			print("not a past device")
			text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
			if(result == True):
				myDevice.add_device(str(text))
				cur = myDevice.get_PM()
				self.pacemaker_number.setText("Patient: "+cur[0])
				config.current_pm(cur[1])
		else:
			cur = myDevice.get_PM()
			self.pacemaker_number.setText("Patient: "+cur[0])
			config.current_pm(cur[1])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_8.setText("")
			last_param = load_current()
			last_param[0] = '7'
			last_param[1] = self.LRL_Current.text()
			last_param[2] = self.URL_Current.text()
			last_param[14] = self.VA_Current.text()
			last_param[9] = self.VPW_Current.text()
			last_param[3] = self.MSR_Current.text()
			last_param[4] = self.AT_Current.text()
			last_param[5] = self.RT_Current.text()
			last_param[6] = self.RF_Current.text()
			last_param[7] = self.RCT_Current.text()
			temp = copy.deepcopy(last_param)
			mySerial.open_serial()	
			send = mySerial.send_data(temp)
			mySerial.close_serial()
			if(send):
				self.clear_inputs()
				self.update_patient()
				update_text(last_param)
				global status
				status = 1
				self.connected.setText("Connected")
				self.disconnected.setText("")
				self.conn_error.setText("")
				print(last_param)	
			else:
				status = 0
				self.conn_error.setText("Check Connection")
				self.disconnected.setText("Disconnected")
				self.connected.setText("")
				self.pacemaker_number.setText("")
		else:
			self.INVALID_8.setText("*Please confirm changes")

	def get_from_pm(self):
		mySerial.open_serial()
		recieved = mySerial.get_param()
		mySerial.close_serial()
		if(recieved):
			global status
			status = 1
			self.update_patient()
			update_text(recieved)
			self.mode_check()
			self.current_param()
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.conn_error.setText("")
			self.clear_inputs()
		else:
			status = 0
			self.conn_error.setText("Check Connection")
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")

	def clear_inputs(self):
		User = [self.LRL, self.URL,self.VA,self.VPW,self.MSR,self.AT,self.RT,self.RF,self.RCT]
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5, self.INVALID_6, self.INVALID_9,self.INVALID_10,self.INVALID_11]
		clear_box(User,Label)


class vvir_mode(QDialog):
	def __init__(self):
		# get param list from_serial(param)
		super(vvir_mode, self).__init__()
		loadUi("interface/vvir_mode.ui", self)
		if(status):
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.update_patient()
		else:
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")
		self.current_param()
		self.update_pm.clicked.connect(self.send_to_pm)
		self.refresh.clicked.connect(self.get_from_pm)
		self.logout.clicked.connect(self.go_to_logout)
		self.account.clicked.connect(self.go_to_account)
		self.no_pacing.clicked.connect(self.go_to_no)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.aoor.clicked.connect(self.go_to_aoor)
		self.aair.clicked.connect(self.go_to_aair)
		self.voor.clicked.connect(self.go_to_voor)
		self.doo.clicked.connect(self.go_to_doo)
		self.door.clicked.connect(self.go_to_door)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.current_param) 
		self.clear.clicked.connect(self.clear_inputs)
	def mode_check(self):
		last_param = load_current()
		if(last_param[0] == '1'):
			aoo = aoo_mode()
			go_to_page(aoo)		
		elif(last_param[0] == '2'):
			aai = aai_mode()
			go_to_page(aai)			
		elif(last_param[0] == '3'):
			aoor = aoor_mode()
			go_to_page(aoor)		
		elif(last_param[0] == '4'):
			aair = aair_mode()
			go_to_page(aair)
		elif(last_param[0] == '5'):
			voo = voo_mode()
			go_to_page(voo)
		elif(last_param[0] == '6'):
			vvi = vvi_mode()
			go_to_page(vvi)
		elif(last_param[0] == '7'):
			voor = voor_mode()
			go_to_page(voor)
		elif(last_param[0] == '8'):
			vvir = vvir_mode()
			go_to_page(vvir)
		elif(last_param[0] == '9'):
			door = door_mode()
			go_to_page(door)
		elif(last_param[0] == '10'):
			doo = doo_mode()
			go_to_page(doo)
		else:
			no = no_pace()
			go_to_page(no)

	def go_to_no(self): 
		no = no_pace()
		go_to_page(no)

	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)	

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)			

	def go_to_aoor(self): 
		aoor = aoor_mode()
		go_to_page(aoor)

	def go_to_aair(self): 
		aair = aair_mode()
		go_to_page(aair)

	def go_to_voor(self): 
		voor = voor_mode()
		go_to_page(voor)

	def go_to_doo(self): 
		doo = doo_mode()
		go_to_page(doo)

	def go_to_door(self): 
		door = door_mode()
		go_to_page(door)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	def go_to_account(self):
		account_var = account.account_page()
		go_to_page(account_var)


	def current_param(self):
		self.user_display.setText("User: "+config.is_current_user())
		# self.pacemaker_number.setText("Pacemaker ID: "+config.is_current_pm())
		last_param = load_current()
		self.LRL_Current.setText(last_param[1]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(last_param[2])
		self.VA_Current.setText(last_param[14])
		self.VPW_Current.setText(last_param[9])
		self.VRP_Current.setText(last_param[11])
		self.MSR_Current.setText(last_param[3])
		self.AT_Current.setText(last_param[4])
		self.RT_Current.setText(last_param[5])
		self.RF_Current.setText(last_param[6])
		self.RCT_Current.setText(last_param[7])

	
	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.VA.currentText(),self.VPW.currentText(),self.MSR.currentText(),self.AT.currentText(),self.RT.currentText(),self.RF.currentText(),self.RCT.currentText(),self.VRP.currentText()]
		Current = [self.LRL_Current, self.URL_Current,self.VA_Current,self.VPW_Current, self.MSR_Current, self.AT_Current, self.RT_Current, self.RF_Current, self.RCT_Current, self.VRP_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5, self.INVALID_6, self.INVALID_7,self.INVALID_9,self.INVALID_10,self.INVALID_11]
		update_current(User, Current, Label)

	def update_patient(self):
		if(myDevice.get_PM()[0]==0):
			print("not a past device")
			text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
			if(result == True):
				myDevice.add_device(str(text))
				cur = myDevice.get_PM()
				self.pacemaker_number.setText("Patient: "+cur[0])
				config.current_pm(cur[1])
		else:
			cur = myDevice.get_PM()
			self.pacemaker_number.setText("Patient: "+cur[0])
			config.current_pm(cur[1])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_8.setText("")
			last_param = load_current()
			last_param[0] = '8'
			last_param[1] = self.LRL_Current.text()
			last_param[2] = self.URL_Current.text()
			last_param[14] = self.VA_Current.text()
			last_param[9] = self.VPW_Current.text()
			last_param[11] = self.VRP_Current.text()
			last_param[3] = self.MSR_Current.text()
			last_param[4] = self.AT_Current.text()
			last_param[5] = self.RT_Current.text()
			last_param[6] = self.RF_Current.text()
			last_param[7] = self.RCT_Current.text()
			temp = copy.deepcopy(last_param)
			mySerial.open_serial()	
			send = mySerial.send_data(temp)
			mySerial.close_serial()
			if(send):
				self.clear_inputs()
				self.update_patient()
				update_text(last_param)
				global status
				status = 1
				self.connected.setText("Connected")
				self.disconnected.setText("")
				self.conn_error.setText("")
				print(last_param)	
			else:
				status = 0
				self.conn_error.setText("Check Connection")
				self.disconnected.setText("Disconnected")
				self.connected.setText("")
				self.pacemaker_number.setText("")
		else:
			self.INVALID_8.setText("*Please confirm changes")
	
	def get_from_pm(self):
		mySerial.open_serial()
		recieved = mySerial.get_param()
		mySerial.close_serial()
		if(recieved):
			global status
			status = 1
			self.update_patient()
			update_text(recieved)
			self.mode_check()
			self.current_param()
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.conn_error.setText("")
			self.clear_inputs()
		else:
			status = 0
			self.conn_error.setText("Check Connection")
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")


	def clear_inputs(self):
		User = [self.LRL, self.URL,self.VA,self.VPW,self.MSR,self.AT,self.RT,self.RF,self.RCT,self.VRP]
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5, self.INVALID_6, self.INVALID_7,self.INVALID_9,self.INVALID_10,self.INVALID_11]
		clear_box(User,Label)

class doo_mode(QDialog):
	def __init__(self):
		# get param list from_serial(param)
		super(doo_mode, self).__init__()
		loadUi("interface/doo_mode.ui", self)
		if(status):
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.update_patient()
		else:
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")
		self.current_param()
		self.update_pm.clicked.connect(self.send_to_pm)
		self.refresh.clicked.connect(self.get_from_pm)
		self.logout.clicked.connect(self.go_to_logout)
		self.account.clicked.connect(self.go_to_account)
		self.no_pacing.clicked.connect(self.go_to_no)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.aoor.clicked.connect(self.go_to_aoor)
		self.aair.clicked.connect(self.go_to_aair)
		self.voor.clicked.connect(self.go_to_voor)
		self.vvir.clicked.connect(self.go_to_vvir)
		self.door.clicked.connect(self.go_to_door)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.current_param) 
		self.clear.clicked.connect(self.clear_inputs)
	
	def mode_check(self):
		last_param = load_current()
		if(last_param[0] == '1'):
			aoo = aoo_mode()
			go_to_page(aoo)		
		elif(last_param[0] == '2'):
			aai = aai_mode()
			go_to_page(aai)			
		elif(last_param[0] == '3'):
			aoor = aoor_mode()
			go_to_page(aoor)		
		elif(last_param[0] == '4'):
			aair = aair_mode()
			go_to_page(aair)
		elif(last_param[0] == '5'):
			voo = voo_mode()
			go_to_page(voo)
		elif(last_param[0] == '6'):
			vvi = vvi_mode()
			go_to_page(vvi)
		elif(last_param[0] == '7'):
			voor = voor_mode()
			go_to_page(voor)
		elif(last_param[0] == '8'):
			vvir = vvir_mode()
			go_to_page(vvir)
		elif(last_param[0] == '9'):
			door = door_mode()
			go_to_page(door)
		elif(last_param[0] == '10'):
			doo = doo_mode()
			go_to_page(doo)
		else:
			no = no_pace()
			go_to_page(no)


	def go_to_no(self): 
		no = no_pace()
		go_to_page(no)

	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)	

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)			

	def go_to_aoor(self): 
		aoor = aoor_mode()
		go_to_page(aoor)

	def go_to_aair(self): 
		aair = aair_mode()
		go_to_page(aair)

	def go_to_voor(self): 
		voor = voor_mode()
		go_to_page(voor)

	def go_to_vvir(self): 
		vvir = vvir_mode()
		go_to_page(vvir)

	def go_to_door(self): 
		door = door_mode()
		go_to_page(door)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	def go_to_account(self):
		account_var = account.account_page()
		go_to_page(account_var)

	def current_param(self):
		self.user_display.setText("User: "+config.is_current_user())
		# self.pacemaker_number.setText("Pacemaker ID: "+config.is_current_pm())
		last_param = load_current()
		self.LRL_Current.setText(last_param[1]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(last_param[2])
		self.AA_Current.setText(last_param[13])
		self.APW_Current.setText(last_param[8])
		self.VA_Current.setText(last_param[14])
		self.VPW_Current.setText(last_param[9])		
		self.FAVD_Current.setText(last_param[12])		
		
	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.AA.currentText(),self.APW.currentText(),self.VA.currentText(),self.VPW.currentText(),self.FAVD.currentText()]
		Current = [self.LRL_Current, self.URL_Current,self.AA_Current,self.APW_Current,self.VA_Current,self.VPW_Current,self.FAVD_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_6,self.INVALID_7,self.INVALID_8]
		update_current(User, Current, Label)

	def update_patient(self):
		if(myDevice.get_PM()[0]==0):
			print("not a past device")
			text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
			if(result == True):
				myDevice.add_device(str(text))
				cur = myDevice.get_PM()
				self.pacemaker_number.setText("Patient: "+cur[0])
				config.current_pm(cur[1])
		else:
			cur = myDevice.get_PM()
			self.pacemaker_number.setText("Patient: "+cur[0])
			config.current_pm(cur[1])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_5.setText("")
			last_param = load_current()
			last_param[0] = '10'
			last_param[1] = self.LRL_Current.text()
			last_param[2] = self.URL_Current.text()
			last_param[13] = self.AA_Current.text()
			last_param[8] = self.APW_Current.text()
			last_param[14] = self.VA_Current.text()
			last_param[9] = self.VPW_Current.text()
			last_param[12] = self.FAVD_Current.text()	
			temp = copy.deepcopy(last_param)
			mySerial.open_serial()	
			send = mySerial.send_data(temp)
			mySerial.close_serial()
			if(send):
				self.clear_inputs()
				self.update_patient()
				update_text(last_param)
				global status
				status = 1
				self.connected.setText("Connected")
				self.disconnected.setText("")
				self.conn_error.setText("")
				print(last_param)	
			else:
				status = 0
				self.conn_error.setText("Check Connection")
				self.disconnected.setText("Disconnected")
				self.connected.setText("")
				self.pacemaker_number.setText("")
		else:
			self.INVALID_5.setText("*Please confirm changes")

	def get_from_pm(self):
		mySerial.open_serial()
		recieved = mySerial.get_param()
		mySerial.close_serial()
		if(recieved):
			global status
			status = 1
			self.update_patient()
			update_text(recieved)
			self.mode_check()
			self.current_param()
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.conn_error.setText("")
			self.clear_inputs()
		else:
			status = 0
			self.conn_error.setText("Check Connection")
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")

	def clear_inputs(self):
		User = [self.LRL, self.URL,self.AA,self.APW,self.VA,self.VPW,self.FAVD]
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_6,self.INVALID_7,self.INVALID_8]
		clear_box(User,Label)


class door_mode(QDialog):
	def __init__(self):
		# get param list from_serial(param)
		super(door_mode, self).__init__()
		loadUi("interface/door_mode.ui", self)
		if(status):
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.update_patient()
		else:
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")
		self.current_param()
		self.update_pm.clicked.connect(self.send_to_pm)
		self.refresh.clicked.connect(self.get_from_pm)
		self.logout.clicked.connect(self.go_to_logout)
		self.account.clicked.connect(self.go_to_account)
		self.no_pacing.clicked.connect(self.go_to_no)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.aoor.clicked.connect(self.go_to_aoor)
		self.aair.clicked.connect(self.go_to_aair)
		self.voor.clicked.connect(self.go_to_voor)
		self.vvir.clicked.connect(self.go_to_vvir)
		self.doo.clicked.connect(self.go_to_doo)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.current_param) 
		self.clear.clicked.connect(self.clear_inputs)
	
	def mode_check(self):
		last_param = load_current()
		if(last_param[0] == '1'):
			aoo = aoo_mode()
			go_to_page(aoo)		
		elif(last_param[0] == '2'):
			aai = aai_mode()
			go_to_page(aai)			
		elif(last_param[0] == '3'):
			aoor = aoor_mode()
			go_to_page(aoor)		
		elif(last_param[0] == '4'):
			aair = aair_mode()
			go_to_page(aair)
		elif(last_param[0] == '5'):
			voo = voo_mode()
			go_to_page(voo)
		elif(last_param[0] == '6'):
			vvi = vvi_mode()
			go_to_page(vvi)
		elif(last_param[0] == '7'):
			voor = voor_mode()
			go_to_page(voor)
		elif(last_param[0] == '8'):
			vvir = vvir_mode()
			go_to_page(vvir)
		elif(last_param[0] == '9'):
			door = door_mode()
			go_to_page(door)
		elif(last_param[0] == '10'):
			doo = doo_mode()
			go_to_page(doo)
		else:
			no = no_pace()
			go_to_page(no)

	def go_to_no(self): 
		no = no_pace()
		go_to_page(no)

	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)	

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)			

	def go_to_aoor(self): 
		aoor = aoor_mode()
		go_to_page(aoor)

	def go_to_aair(self): 
		aair = aair_mode()
		go_to_page(aair)

	def go_to_voor(self): 
		voor = voor_mode()
		go_to_page(voor)

	def go_to_vvir(self): 
		vvir = vvir_mode()
		go_to_page(vvir)

	def go_to_doo(self): 
		doo = doo_mode()
		go_to_page(doo)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	def go_to_account(self):
		account_var = account.account_page()
		go_to_page(account_var)


	def current_param(self):
		self.user_display.setText("User: "+config.is_current_user())
		# self.pacemaker_number.setText("Pacemaker ID: "+config.is_current_pm())
		last_param = load_current()
		self.LRL_Current.setText(last_param[1]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(last_param[2])
		self.AA_Current.setText(last_param[13])
		self.APW_Current.setText(last_param[8])
		self.VA_Current.setText(last_param[14])
		self.VPW_Current.setText(last_param[9])		
		self.FAVD_Current.setText(last_param[12])
		self.MSR_Current.setText(last_param[3])
		self.AT_Current.setText(last_param[4])
		self.RT_Current.setText(last_param[5])
		self.RF_Current.setText(last_param[6])
		self.RCT_Current.setText(last_param[7])
	
	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.AA.currentText(),self.APW.currentText(),self.VA.currentText(),self.VPW.currentText(),self.RT.currentText(),self.RF.currentText(),self.RCT.currentText(),self.AT.currentText(),self.MSR.currentText(),self.FAVD.currentText()]
		Current = [self.LRL_Current, self.URL_Current,self.AA_Current,self.APW_Current,self.VA_Current,self.VPW_Current, self.RT_Current, self.RF_Current, self.RCT_Current, self.AT_Current, self.MSR_Current,self.FAVD_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5, self.INVALID_6,self.INVALID_7, self.INVALID_9,self.INVALID_10,self.INVALID_11,self.INVALID_12,self.INVALID_13]
		update_current(User, Current, Label)

	def update_patient(self):
		if(myDevice.get_PM()[0]==0):
			print("not a past device")
			text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
			if(result == True):
				myDevice.add_device(str(text))
				cur = myDevice.get_PM()
				self.pacemaker_number.setText("Patient: "+cur[0])
				config.current_pm(cur[1])
		else:
			cur = myDevice.get_PM()
			self.pacemaker_number.setText("Patient: "+cur[0])
			config.current_pm(cur[1])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_8.setText("")
			last_param = load_current()
			last_param[0] = '9'
			last_param[1] = self.LRL_Current.text()
			last_param[2] = self.URL_Current.text()
			last_param[13] = self.AA_Current.text()
			last_param[8] = self.APW_Current.text()
			last_param[14] = self.VA_Current.text()
			last_param[9] = self.VPW_Current.text()
			last_param[12] = self.FAVD_Current.text()			
			last_param[3] = self.MSR_Current.text()
			last_param[4] = self.AT_Current.text()
			last_param[5] = self.RT_Current.text()
			last_param[6] = self.RF_Current.text()
			last_param[7] = self.RCT_Current.text()

			temp = copy.deepcopy(last_param)
			mySerial.open_serial()	
			send = mySerial.send_data(temp)
			mySerial.close_serial()
			if(send):
				self.clear_inputs()
				self.update_patient()
				update_text(last_param)
				global status
				status = 1
				self.connected.setText("Connected")
				self.disconnected.setText("")
				self.conn_error.setText("")
				print(last_param)	
			else:
				status = 0
				self.conn_error.setText("Check Connection")
				self.disconnected.setText("Disconnected")
				self.connected.setText("")
				self.pacemaker_number.setText("")
		else:
			self.INVALID_8.setText("*Please confirm changes")

	def get_from_pm(self):
		mySerial.open_serial()
		recieved = mySerial.get_param()
		mySerial.close_serial()
		if(recieved):
			global status
			status = 1
			self.update_patient()
			update_text(recieved)
			self.mode_check()
			self.current_param()
			self.connected.setText("Connected")
			self.disconnected.setText("")
			self.conn_error.setText("")
			self.clear_inputs()
		else:
			status = 0
			self.conn_error.setText("Check Connection")
			self.disconnected.setText("Disconnected")
			self.connected.setText("")
			self.pacemaker_number.setText("")

	def clear_inputs(self):
		User = [self.LRL, self.URL,self.AA,self.APW,self.VA,self.VPW,self.RT,self.RF,self.RCT,self.AT,self.MSR,self.FAVD]
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5, self.INVALID_6,self.INVALID_7, self.INVALID_9,self.INVALID_10,self.INVALID_11,self.INVALID_12,self.INVALID_13]
		clear_box(User,Label)
