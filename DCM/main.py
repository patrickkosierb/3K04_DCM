from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget	
import sys
import sqlite3
import os

#welcome/login screen
class WelcomeScreen(QDialog): #welcome/login screen
	def __init__(self): #consstructor: checks login credentials goes to main menu if login; user can register;
		super(WelcomeScreen, self).__init__()
		loadUi("interface/welcome_screen.ui", self) 
		self.password.setEchoMode(QtWidgets.QLineEdit.Password) #sets password to dots
		self.login.clicked.connect(self.go_to_menu) #TEMP FOR TESTING MODES
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
		new_user = new_user()
		widget.addWidget(menu)
		widget.setCurrentIndex(widget.currentIndex()+1)			
	
	#goes to main menu 
	def go_to_menu(self): #goes to main menu; should then go to mode pages? 
		menu = main_menu()
		widget.addWidget(menu)
		widget.setCurrentIndex(widget.currentIndex()+1)

#main menu screen
class main_menu(QDialog): #main menu screen
	def __init__(self):
		super(main_menu, self).__init__()
		loadUi("interface/main_menu.ui", self)	
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)

	def go_to_aoo(self): #goes to main menu; should then go to mode pages? 
		aoo = aoo_mode()
		widget.addWidget(aoo)
		widget.setCurrentIndex(widget.currentIndex()+1)
	
	def go_to_aai(self): #goes to main menu; should then go to mode pages? 
		aai = aai_mode()
		widget.addWidget(aai)
		widget.setCurrentIndex(widget.currentIndex()+1)
	#def logout(self):
		# widget.setCurrentIndex(widget.currentIndex()-1)		

#registration screen
class new_user(QDialog): #registration screen
	def __init__(self):
		super(new_user, self).__init__()
		loadUi("interface/new_user.ui", self)


#aoo mode screen
class aoo_mode(QDialog):
	def __init__(self):
		super(aoo_mode, self).__init__()
		loadUi("interface/aoo_mode.ui", self)
		self.aai.clicked.connect(self.go_to_aai)
		self.get_current_param()



	def go_to_aai(self): 
		aai = aai_mode()
		widget.addWidget(aai)
		widget.setCurrentIndex(widget.currentIndex()+1)	

	def get_current_param(self):
		#uses file io functions to take CURRENT parameters and load them into the text boxes
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(param[1])
		self.AA_Current.setText(param[2])


class aai_mode(QDialog):
	def __init__(self):
		super(aai_mode, self).__init__()
		loadUi("interface/aai_mode.ui", self)




app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
welcome = WelcomeScreen()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
sys.exit(app.exec_())
