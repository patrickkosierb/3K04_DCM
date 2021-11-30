from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget
# import sys
# import sqlite3
# import os
import string
import config
import menu
import devices
from helpers import go_to_page

myDevice = devices.Device()

# change to about
class account_page(QDialog): 
    def __init__(self):
        super(account_page, self).__init__()
        loadUi("interface/account_page.ui", self)
        self.username.setText(config.is_current_user())
        name = myDevice.get_PM()[0]
        self.pm_no.setText(name)
       	self.pm_id.setText(myDevice.Get_Current_ID()[0])
        self.password.setEchoMode(QtWidgets.QLineEdit.Password) 
        self.password_confirm.setEchoMode(QtWidgets.QLineEdit.Password) 
        self.changes.clicked.connect(self.change_username)
        self.back.clicked.connect(self.go_to_menu)


    def go_to_menu(self):
        menu_var = menu.main_menu()
        go_to_page(menu_var)

    def change_username(self):
    	if(self.checkBox.isChecked()):
	    	db = open("data/users.txt","r")
	    	new_user = self.username_new.text()
	    	password = self.password.text()
	    	password2 = self.password_confirm.text()
	    	d = []
	    	f = []
	    	for i in db:
	    		l = i.split(", ")
	    		l[1] = l[1].strip()
	    		d.append(l[0])
	    		f.append(l[1])
	    	if password!=password2:
	    		self.invalid_up2.setText("Passwords dont match")
	    	elif password not in f:
	    		self.invalid_up2.setText("Incorrect Password")
	    	elif new_user in d:
	    		self.invalid_up2.setText("Username exists")
	    	elif len(new_user)==0 or len(password) == 0:
	     		self.invalid_up2.setText("Please input all fields")
	    	else:
	    		db = open("data/users.txt",'r')
	    		lines = db.readlines()

	    		lines[int(config.is_line())-1] = new_user+", "+config.is_password()+", "+str(config.is_line())+'\n'
	    		config.current_user(new_user)
	    		db = open("data/users.txt","w")
	    		db.writelines(lines)
	    		db.close()
	    		self.username.setText(config.is_current_user())
	    		self.invalid_up2.setText("")
	    		self.invalid_up3.setText("Chagnes successfully applied")
    	else:
    		self.invalid_up2.setText("")
    		self.invalid_up2.setText("Please confirm changes")
