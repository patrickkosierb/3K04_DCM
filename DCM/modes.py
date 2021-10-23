# @ file: mode.py
# @ brief: mode file contains all mode classes (AOO AAI VOO VII)
# @ note: missing file io stuff and logout button

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget	
import sys
import sqlite3
import os
import string

import config
import menu
import welcome
from helpers import go_to_page, update_current, clear_box

param_atr = ['0', '0', '0', '0','0', '0', '0']
param_vent = ['0', '0', '0', '0','0', '0', '0']

# ATRIAL
class aoo_mode(QDialog):
	def __init__(self):
		# get param list from_serial(param)
		super(aoo_mode, self).__init__()
		loadUi("interface/aoo_mode.ui", self)
		self.current_param()
		self.logout.clicked.connect(self.go_to_logout)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.reset_param) #current_param
		self.update_pm.clicked.connect(self.send_to_pm)
		self.clear.clicked.connect(self.clear_inputs)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	# uses file io functions to take CURRENT parameters TAKEN FROM PACEMAKER and load them into the text boxes
	def current_param(self):
		self.LRL_Current.setText(param_atr[0]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(param_atr[1])
		self.AA_Current.setText(param_atr[2])
		self.APW_Current.setText(param_atr[3])

	
	# update the current parameters, apply changes is only for ui, send to pacemaker will actually update pacemaker
	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.AA.currentText(),self.APW.currentText()];
		Current = [self.LRL_Current, self.URL_Current,self.AA_Current,self.APW_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4]
		update_current(User, Current, Label)


	def reset_param(self):
		#access text file again, this differs from current_param because now we're getting the old values of param_mode
		self.LRL_Current.setText(param_atr[0]) 
		self.URL_Current.setText(param_atr[1])
		self.AA_Current.setText(param_atr[2])
		self.APW_Current.setText(param_atr[3])

	#take current and update text file
	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_5.setText("")
			param_atr[0] = self.LRL_Current.text()
			param_atr[1] = self.URL_Current.text()
			param_atr[2] = self.AA_Current.text()
			param_atr[3] = self.APW_Current.text()
			print(param_atr)
		else:
			self.INVALID_5.setText("*Please confirm changes")

	def clear_inputs(self):
		User = [self.LRL, self.URL,self.AA,self.APW];
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4]
		clear_box(User,Label)


class aai_mode(QDialog):
	def __init__(self):
		super(aai_mode, self).__init__()
		loadUi("interface/aai_mode.ui", self)
		self.current_param()
		self.logout.clicked.connect(self.go_to_logout)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.reset_param)
		self.update_pm.clicked.connect(self.send_to_pm)
		self.clear.clicked.connect(self.clear_inputs)
		
	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	def current_param(self):
		self.LRL_Current.setText(param_atr[0]) 
		self.URL_Current.setText(param_atr[1])
		self.AA_Current.setText(param_atr[2])
		self.APW_Current.setText(param_atr[3]) 
		self.AS_Current.setText(param_atr[4])
		self.ARP_Current.setText(param_atr[5])
		self.PVARP_Current.setText(param_atr[6])
	
	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.AA.currentText(),self.APW.currentText(),self.AS.currentText(),self.ARP.currentText(),self.PVARP.currentText()]
		Current = [self.LRL_Current, self.URL_Current,self.AA_Current,self.APW_Current,self.AS_Current,self.ARP_Current,self.PVARP_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5,self.INVALID_6,self.INVALID_7]
		update_current(User, Current, Label)

	def reset_param(self):
		self.LRL_Current.setText(param_atr[0]) 
		self.URL_Current.setText(param_atr[1])
		self.AA_Current.setText(param_atr[2])
		self.APW_Current.setText(param_atr[3]) 
		self.AS_Current.setText(param_atr[4])
		self.ARP_Current.setText(param_atr[5])
		self.PVARP_Current.setText(param_atr[6])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_8.setText("")
			param_atr[0] = self.LRL_Current.text()
			param_atr[1] = self.URL_Current.text()
			param_atr[2] = self.AA_Current.text()
			param_atr[3] = self.APW_Current.text()
			param_atr[4] = self.AS_Current.text()
			param_atr[5] = self.ARP_Current.text()
			param_atr[6] = self.PVARP_Current.text()
			print(param_atr)
		else:
			self.INVALID_8.setText("*Please confirm changes")

	def clear_inputs(self):
		User = [self.LRL, self.URL,self.AA,self.APW,self.AS,self.ARP,self.PVARP]
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5,self.INVALID_6,self.INVALID_7]
		clear_box(User,Label)

# VENTRICLE 

class voo_mode(QDialog):
	def __init__(self):
		super(voo_mode, self).__init__()
		loadUi("interface/voo_mode.ui", self)
		self.current_param()
		self.logout.clicked.connect(self.go_to_logout)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.reset_param)
		self.update_pm.clicked.connect(self.send_to_pm)
		self.clear.clicked.connect(self.clear_inputs)

	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_vvi(self): 
		vvi = vvi_mode()
		go_to_page(vvi)

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)
	
	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)
	
	def current_param(self):
		self.LRL_Current.setText(param_vent[0]) 
		self.URL_Current.setText(param_vent[1])
		self.VA_Current.setText(param_vent[2])
		self.VPW_Current.setText(param_vent[3])

	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.VA.currentText(),self.VPW.currentText()]
		Current = [self.LRL_Current, self.URL_Current,self.VA_Current,self.VPW_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4]
		update_current(User, Current, Label)

	def reset_param(self):
		#access text file again
		self.LRL_Current.setText(param_vent[0]) 
		self.URL_Current.setText(param_vent[1])
		self.VA_Current.setText(param_vent[2])
		self.VPW_Current.setText(param_vent[3])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_5.setText("")
			param_vent[0] = self.LRL_Current.text()
			param_vent[1] = self.URL_Current.text()
			param_vent[2] = self.VA_Current.text()
			param_vent[3] = self.VPW_Current.text()
			print(param_vent)
		else:
			self.INVALID_5.setText("*Please confirm changes")
	
	def clear_inputs(self):
		User = [self.LRL, self.URL,self.VA,self.VPW]
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4]
		clear_box(User,Label)

class vvi_mode(QDialog):
	def __init__(self):
		super(vvi_mode, self).__init__()
		loadUi("interface/vvi_mode.ui", self)
		self.current_param()
		self.logout.clicked.connect(self.go_to_logout)
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.reset_param)
		self.update_pm.clicked.connect(self.send_to_pm)
		self.clear.clicked.connect(self.clear_inputs)
		
	def go_to_logout(self): 
		welcome_var = welcome.WelcomeScreen()
		go_to_page(welcome_var)

	def go_to_aoo(self): 
		aoo = aoo_mode()
		go_to_page(aoo)

	def go_to_aai(self): 
		aai = aai_mode()
		go_to_page(aai)

	def go_to_voo(self): 
		voo = voo_mode()
		go_to_page(voo)	

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def current_param(self):
		self.LRL_Current.setText(param_vent[0]) 
		self.URL_Current.setText(param_vent[1])
		self.VA_Current.setText(param_vent[2])
		self.VPW_Current.setText(param_vent[3])
		self.VS_Current.setText(param_vent[4]) 
		self.VRP_Current.setText(param_vent[5])
		self.PVARP_Current.setText(param_vent[6])

	def update_param(self):
		User = [self.LRL.currentText(), self.URL.currentText(),self.VA.currentText(),self.VPW.currentText(),self.VS.currentText(),self.VRP.currentText(),self.PVARP.currentText()]
		Current = [self.LRL_Current, self.URL_Current,self.VA_Current,self.VPW_Current,self.VS_Current,self.VRP_Current,self.PVARP_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5,self.INVALID_6,self.INVALID_7]
		update_current(User, Current, Label)
		
	def reset_param(self):
		self.LRL_Current.setText(param_vent[0]) 
		self.URL_Current.setText(param_vent[1])
		self.VA_Current.setText(param_vent[2])
		self.VPW_Current.setText(param_vent[3])
		self.VS_Current.setText(param_vent[4]) 
		self.VRP_Current.setText(param_vent[5])
		self.PVARP_Current.setText(param_vent[6])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_8.setText("")
			param_vent[0] = self.LRL_Current.text()
			param_vent[1] = self.URL_Current.text()
			param_vent[2] = self.VA_Current.text()
			param_vent[3] = self.VPW_Current.text()
			param_vent[4] = self.VS_Current.text()
			param_vent[5] = self.VRP_Current.text()
			param_vent[6] = self.PVARP_Current.text()
			print(param_vent)
		else:
			self.INVALID_8.setText("*Please confirm changes")
	
	def clear_inputs(self):
		User = [self.LRL, self.URL,self.VA,self.VPW,self.VS,self.VRP,self.PVARP]
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5,self.INVALID_6,self.INVALID_7]
		clear_box(User,Label)