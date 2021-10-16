# @ file: main.py
# @ brief: main file runs welcome screen, begins state flow


import sys
import os
import string

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget	


import config
from welcome import WelcomeScreen


app = QApplication(sys.argv)
config.init()
welcome = WelcomeScreen()
config.widget.addWidget(welcome)
config.widget.setFixedHeight(800)
config.widget.setFixedWidth(1200)
config.widget.show()
sys.exit(app.exec_())
