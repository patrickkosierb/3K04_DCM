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
		self.login.clicked.connect(self.go_to_menu) #TEMP FOR TESTING MODES
		self.newuser.clicked.connect(self.go_to_newuser) #TEMP FOR TESTING MODES

		#if new user is pressed go to next screen
		
	#checks if username and password are in data base then goes to menu 
	def login_check(self): #checks login
		user = self.username.text()
		password = self.password.text()
		# self.invalid_up.setText("Invalid username or Password")
		#if username and password match that of something in the text file, login works
		#else, invalid password or username
		#blank, please write something or register new user
		#if true -> self.go_to_menu()

	#goes to registration screen then back to login or main menu?
	def go_to_newuser(self): #goes to registration screen; should then go to menu and saves credentials to .txt
		newuser = new_user()
		go_to_page(newuser)

	#goes to main menu 
	def go_to_menu(self): #goes to main menu; should then go to mode pages? 
		menu_var = menu.main_menu()
		go_to_page(menu_var)

#registration screen
class new_user(QDialog): #registration screen
	def __init__(self):
		super(new_user, self).__init__()
		loadUi("interface/new_user.ui", self)

		