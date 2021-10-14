from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget	
import sys
import sqlite3
import os


class WelcomeScreen(QDialog): #welcome/login screen
	def __init__(self): #consstructor: checks login credentials goes to main menu if login; user can register;
		super(WelcomeScreen, self).__init__()
		loadUi("interface/welcome_screen.ui", self) 
		self.password.setEchoMode(QtWidgets.QLineEdit.Password) #sets password to dots
		# self.login.clicked.connect(self.go_to_menu)
		#if new user is pressed go to next screen
		

	def login_check(self): #checks login
		user = self.username.text()
		password = self.password.text()
		# self.invalid_up.setText("Invalid username or Password")
		#if username and password match that of something in the text file, login works
		#else, invalid password or username
		#blank, please write something or register new user
		#if true -> self.go_to_menu()

	def go_to_newuser(self): #goes to registration screen; should then go to menu and saves credentials to .txt
		new_user = new_user()
		widget.addWidget(menu)
		widget.setCurrentIndex(widget.currentIndex()+1)			
	
	def go_to_menu(self): #goes to main menu; should then go to mode pages? 
		menu = main_menu()
		widget.addWidget(menu)
		widget.setCurrentIndex(widget.currentIndex()+1)


class main_menu(QDialog): #main menu screen
	def __init__(self):
		super(main_menu, self).__init__()
		loadUi("interface/main_menu.ui", self)	
	
	#def logout(self):
		# widget.setCurrentIndex(widget.currentIndex()-1)		


class new_user(QDialog): #registration screen
	def __init__(self):
		super(new_user, self).__init__()
		loadUi("interface/new_user.ui", self)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
welcome = WelcomeScreen()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
sys.exit(app.exec_())
