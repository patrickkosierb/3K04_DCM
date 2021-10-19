from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget
import sys
import sqlite3
import os
import string

import config
import menu
from helpers import go_to_page

class account_page(QDialog): #main menu screen
    def __init__(self):
        super(account_page, self).__init__()
        loadUi("interface/account_page.ui", self)
        self.back.clicked.connect(self.go_to_menu)
        

    def go_to_menu(self):
        menu_var = menu.main_menu()
        go_to_page(menu_var)


