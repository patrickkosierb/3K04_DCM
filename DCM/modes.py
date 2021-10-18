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
from helpers import go_to_page, update_current
# ATRIAL

class aoo_mode(QDialog):
	def __init__(self):
		# get param list from_serial(param)
		# param = [150 100 200]
		super(aoo_mode, self).__init__()
		loadUi("interface/aoo_mode.ui", self)
		self.current_param()
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.reset_param) #current_param
		self.update_pm.clicked.connect(self.send_to_pm)

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

	# uses file io functions to take CURRENT parameters TAKEN FROM PACEMAKER and load them into the text boxes
	def current_param(self):
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(param[1])
		self.AA_Current.setText(param[2])
	
	# update the current parameters, apply changes is only for ui, send to pacemaker will actually update pacemaker
	def update_param(self):
		User = [self.LRL.text(), self.URL.text(),self.AA.text(),self.APW.text()]
		Current = [self.LRL_Current, self.URL_Current,self.AA_Current,self.APW_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4]
		update_current(User, Current, Label)

	def reset_param(self):
		#access text file again
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) 
		self.URL_Current.setText(param[1])
		self.AA_Current.setText(param[2])

	#take current and update text file
	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_5.setText("")
			param = ['150', '200', '100'] 
			param[0] = self.LRL_Current.text()
			param[1] = self.URL_Current.text()
			param[2] = self.AA_Current.text()
			print(param)
		else:
			self.INVALID_5.setText("*Please confirm changes")

class aai_mode(QDialog):
	def __init__(self):
		super(aai_mode, self).__init__()
		loadUi("interface/aai_mode.ui", self)
		self.current_param()
		self.aoo.clicked.connect(self.go_to_aoo)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.reset_param)
		self.update_pm.clicked.connect(self.send_to_pm)

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

	def current_param(self):
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) 
		self.URL_Current.setText(param[1])
		self.AA_Current.setText(param[2])
	
	def update_param(self):
		User = [self.LRL.text(), self.URL.text(),self.AA.text(),self.APW.text(),self.AS.text(),self.ARP.text(),self.PVARP.text()]
		Current = [self.LRL_Current, self.URL_Current,self.AA_Current,self.APW_Current,self.AS_Current,self.ARP_Current,self.PVARP_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5,self.INVALID_6,self.INVALID_7]
		update_current(User, Current, Label)

	def reset_param(self):
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0])
		self.URL_Current.setText(param[1])
		self.AA_Current.setText(param[2])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_8.setText("")
			param = ['150', '200', '100'] 
			param[0] = self.LRL_Current.text()
			param[1] = self.URL_Current.text()
			param[2] = self.AA_Current.text()
			print(param)
		else:
			self.INVALID_8.setText("*Please confirm changes")


# VENTRICLE 

class voo_mode(QDialog):
	def __init__(self):
		super(voo_mode, self).__init__()
		loadUi("interface/voo_mode.ui", self)
		self.current_param()
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.reset_param)
		self.update_pm.clicked.connect(self.send_to_pm)

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
	
	def current_param(self):
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) 
		self.URL_Current.setText(param[1])
		self.VV_Current.setText(param[2])
	
	def update_param(self):
		User = [self.LRL.text(), self.URL.text(),self.VV.text(),self.VPW.text()]
		Current = [self.LRL_Current, self.URL_Current,self.VV_Current,self.VPW_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4]
		update_current(User, Current, Label)

	def reset_param(self):
		#access text file again
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) 
		self.URL_Current.setText(param[1])
		self.VV_Current.setText(param[2])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_5.setText("")
			param = ['150', '200', '100'] 
			param[0] = self.LRL_Current.text()
			param[1] = self.URL_Current.text()
			param[2] = self.VV_Current.text()
			print(param)
		else:
			self.INVALID_5.setText("*Please confirm changes")

class vvi_mode(QDialog):
	def __init__(self):
		super(vvi_mode, self).__init__()
		loadUi("interface/vvi_mode.ui", self)
		self.current_param()
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.reset_param)
		self.update_pm.clicked.connect(self.send_to_pm)

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
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) 
		self.URL_Current.setText(param[1])
		self.VV_Current.setText(param[2])

	def update_param(self):
		User = [self.LRL.text(), self.URL.text(),self.VV.text(),self.VPW.text(),self.VS.text(),self.VRP.text(),self.PVARP.text()]
		Current = [self.LRL_Current, self.URL_Current,self.VV_Current,self.VPW_Current,self.VS_Current,self.VRP_Current,self.PVARP_Current] 
		Label = [self.INVALID, self.INVALID_2, self.INVALID_3, self.INVALID_4,self.INVALID_5,self.INVALID_6,self.INVALID_7]
		update_current(User, Current, Label)
		
	def reset_param(self):
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0])
		self.URL_Current.setText(param[1])
		self.VV_Current.setText(param[2])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_8.setText("")
			param = ['150', '200', '100'] 
			param[0] = self.LRL_Current.text()
			param[1] = self.URL_Current.text()
			param[2] = self.VV_Current.text()
			print(param)
		else:
			self.INVALID_8.setText("*Please confirm changes")
