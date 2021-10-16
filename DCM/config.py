# @ file: config.py
# @ brief: holds global variables

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget	

def init():
	global widget
	widget = QtWidgets.QStackedWidget()