# @ file: welcome.py
# @ brief: welcome file has all methods for welcome screen buttons and register screen buttons

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

#welcome/login screen
class WelcomeScreen(QDialog): 
	def __init__(self): #consstructor: checks login credentials goes to main menu if login; user can register;
		super(WelcomeScreen, self).__init__()
		loadUi("interface/welcome_screen.ui", self) 
		self.password.setEchoMode(QtWidgets.QLineEdit.Password) #sets password to dots
		self.login.clicked.connect(self.login_check) #if login button is clicked run login_check() method
		self.newuser.clicked.connect(self.go_to_newuser)

	#checks if username and password are in data base then goes to menu 
	def login_check(self): 
		user = self.username.text()
		password = self.password.text()
		if len(user)==0 or len(password)==0:
			self.invalid_up.setText("Please input all fields")
		else:
			db = open("data/users.txt","r")
			d = []
			f = []
			for i in db:
				l = i.split(", ")		
				l[1]=l[1].strip()
				d.append(l[0])
				f.append(l[1])
			data = dict(zip(d, f))

			try:
				if data[user]:
					try:
						if password == data[user]:
							config.current_user(user)
							config.current_password(password)
							config.current_line(l[2].strip())
							self.go_to_menu()
						else:
							self.invalid_up.setText("Incorrect username or password")
					except:
						self.invalid_up.setText("Incorrect password")
				else:
					self.invalid_up.setText("Username does not exist")
			except:
				self.invalid_up.setText("Username does not exist")


	#goes to registration screen; 
	def go_to_newuser(self): 
		newuser = new_user()
		go_to_page(newuser)		

	#goes to main menu 
	def go_to_menu(self):
		menu_var = menu.main_menu()
		go_to_page(menu_var)

#registration screen
class new_user(QDialog): 
	def __init__(self):
		super(new_user, self).__init__()
		loadUi("interface/new_user.ui", self)
		self.password.setEchoMode(QtWidgets.QLineEdit.Password)
		self.password_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
		self.register_2.clicked.connect(self.register_check)
		self.back.clicked.connect(self.go_to_welcomescreen)

	# checks if someone already registered username
	def register_check(self):
		db = open("data/users.txt","r")
		user = self.username.text()
		password = self.password.text()
		password2 = self.password_confirm.text()
		d = []
		f = []
		l = []
		for i in db:
			l = i.split(", ")	
			l[1]=l[1].strip()
			d.append(l[0])
			f.append(l[1])
		
		data = dict(zip(d, f))
		# if we have more than 10 users registered
		if len(d) >= 11: 
			self.invalid_up2.setText("Maximum number of users")

		else:
			if password!= password2:
				self.invalid_up2.setText("Passwords dont match")
			elif user in d:
				self.invalid_up2.setText("Username exists")
			elif len(user)==0 or len(password)==0:
				self.invalid_up2.setText("Please input all fields")
			else:
				db = open("data/users.txt","a")
				db.write("\n"+user+", "+password+", "+str(len(d)+1))
				config.current_user(user)
				config.current_password(password)
				config.current_line(len(d)+1)
				self.go_to_menu()
					
	def go_to_menu(self): 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

	def go_to_welcomescreen(self):
		welcomescreen = WelcomeScreen()
		go_to_page(welcomescreen)
	
				# a,b = i.split(", ")
				# b=b.strip()
				# d.append(a)
				# f.append(b)