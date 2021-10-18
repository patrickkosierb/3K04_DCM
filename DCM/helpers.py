# @ file: helpers.py
# @ brief: helpers file contains functionality common accross all modules

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget	
import config

def go_to_page(page): 
	config.widget.addWidget(page)
	config.widget.setCurrentIndex(config.widget.currentIndex()+1)

# checks if user input is a number, then sets current pacemaker parameter text box to the input
def check_and_update(user, current, label):
	if(user.isdigit() and int(user)<255):
		current.setText(user)
		label.setText("")
	elif(user == ""):
		label.setText("")		
	else:
		label.setText("Invalid*")

# updates lists of values
def update_current(user, current, label):
	for i in range(0,len(user)):
		check_and_update(user[i], current[i], label[i])