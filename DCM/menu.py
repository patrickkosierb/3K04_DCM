from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget	
import sys
import sqlite3
import os
import string

import config
from modes import aoo_mode, aai_mode

class main_menu(QDialog): #main menu screen
	def __init__(self):
		super(main_menu, self).__init__()
		loadUi("interface/main_menu.ui", self)	
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)

	def go_to_aoo(self): 
		aoo = aoo_mode()
		config.widget.addWidget(aoo)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)
	
	def go_to_aai(self): 
		aai = aai_mode()
		config.widget.addWidget(aai)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)
	
