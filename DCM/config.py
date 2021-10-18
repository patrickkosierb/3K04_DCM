# @ file: config.py
# @ brief: holds global variables and common functions

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget	

def init():
	global widget
	widget = QtWidgets.QStackedWidget()

