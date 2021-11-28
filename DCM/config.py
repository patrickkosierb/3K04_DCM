# @ file: config.py
# @ brief: holds global variables 
import sys
from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QStackedWidget	
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget	

def init():
	global widget
	widget = QtWidgets.QStackedWidget()
	# global app
	# app = QApplication(sys.argv)
	
def close():
	global app
	sys.exit(app.exec_())

def current_user(user):
	global active_user
	active_user = user

def is_current_user():
	return active_user

def current_pm(pm):
	global active_pm
	active_pm = pm

def is_current_pm():
	return active_pm

def current_password(password):
	global active_password
	active_password = password

def is_password():
	return active_password

def current_line(linenumber):
	global active_line
	active_line = linenumber

def is_line():
	return active_line