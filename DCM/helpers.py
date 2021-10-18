from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget	
import config

def go_to_page(page): 
	config.widget.addWidget(page)
	config.widget.setCurrentIndex(config.widget.currentIndex()+1)

def check_and_update(user, current, label):
	if(user.isdigit() and int(user)<255):
		current.setText(user)
		label.setText("")
	elif(user == ""):
		label.setText("")		
	else:
		label.setText("Invalid*")

def update_current(user, current, label):
	for i in range(0,len(user)):
		check_and_update(user[i], current[i], label[i])