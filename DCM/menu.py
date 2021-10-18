# @ file: menu.py
# @ brief: menu file contains main menu screen class and methods

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget	
import sys
import sqlite3
import os
import string

import config
import modes
import welcome

class main_menu(QDialog): #main menu screen
	def __init__(self):
		super(main_menu, self).__init__()
		loadUi("interface/main_menu.ui", self)	
		self.modes.clicked.connect(self.go_to_modes)
		self.logout.clicked.connect(self.go_to_welcome)
	
	def go_to_modes(self): 
		aoo = modes.aoo_mode()
		config.widget.addWidget(aoo)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)

	def go_to_welcome(self): 
		welcome_var = welcome.WelcomeScreen()
		config.widget.addWidget(welcome_var)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)