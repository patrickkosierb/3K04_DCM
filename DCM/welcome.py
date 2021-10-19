from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget	
import sys
import sqlite3
import os
import string

from helpers import go_to_page
import config
import menu

class WelcomeScreen(QDialog): #welcome/login screen
	def __init__(self): #consstructor: checks login credentials goes to main menu if login; user can register;
		super(WelcomeScreen, self).__init__()
		loadUi("interface/welcome_screen.ui", self) 
		self.password.setEchoMode(QtWidgets.QLineEdit.Password) #sets password to dots
		self.login.clicked.connect(self.login_check) 
		self.newuser.clicked.connect(self.go_to_newuser)

	#checks if username and password are in data base then goes to menu 
	def login_check(self): #checks login
		user = self.username.text()
		password = self.password.text()
		if len(user)==0 or len(password)==0:
			self.invalid_up.setText("Please input all fields")
		else:
			db = open("data/users.txt","r")
			d = []
			f = []
			for i in db:
				a,b = i.split(", ")
				b=b.strip()
				d.append(a)
				f.append(b)
			data = dict(zip(d, f))

			try:
				if data[user]:
					try:
						if password == data[user]:
							self.go_to_menu()
						else:
							self.invalid_up.setText("Incorrect username or password")
					except:
						self.invalid_up.setText("Incorrect password")
				else:
					self.invalid_up.setText("Username does not exist")
			except:
				self.invalid_up.setText("Username does not exist")


	#goes to registration screen then back to login or main menu?
	def go_to_newuser(self): #goes to registration screen; should then go to menu and saves credentials to .txt
		newuser = new_user()
		config.widget.addWidget(newuser)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)			
	
	#goes to main menu 
	def go_to_menu(self): #goes to main menu; should then go to mode pages? 
		menu_var = menu.main_menu()
		config.widget.addWidget(menu_var)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)

#registration screen
class new_user(QDialog): #registration screen
	def __init__(self):
		super(new_user, self).__init__()
		loadUi("interface/new_user.ui", self)
		self.password.setEchoMode(QtWidgets.QLineEdit.Password)
		self.password_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
		self.register_2.clicked.connect(self.register_check)
	def register_check(self):
		db = open("data/users.txt","r")
		user = self.username.text()
		password = self.password.text()
		password2 = self.password_confirm.text()
		d = []
		f = []
		for i in db:
			a,b = i.split(", ")
			b=b.strip()
			d.append(a)
			f.append(b)
		data = dict(zip(d, f))
		if len(data) == 10:
			self.go_to_welcomescreen()
		else:
			if password!= password2:
				self.invalid_up2.setText("Passwords dont match")
			elif user in d :
				self.invalid_up2.setText("Username exists")
			elif len(user)==0 or len(password)==0:
				self.invalid_up2.setText("Please input all fields")
			else:
				db = open("data/users.txt","a")
				db.write("\n"+user+", "+password)
				self.go_to_menu()
				
	def go_to_menu(self): #goes to main menu; should then go to mode pages? 
		menu_var = menu.main_menu()
		config.widget.addWidget(menu_var)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)

	def go_to_welcomescreen(self):
		welcomescreen = WelcomeScreen()
		config.widget.addWidget(welcomescreen)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	
		