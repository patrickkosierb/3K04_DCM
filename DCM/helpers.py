# @ file: helpers.py
# @ brief: helpers file contains functionality common accross all modules

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget	
import config

# checks if string is int or float
def isDigit(x):
	try:
		float(x)
		return True
	except ValueError:
		return False

# widget stack acts like a linear list which adds a new "page" everytime index is incremented
def go_to_page(page): 
	config.widget.addWidget(page)
	config.widget.setCurrentIndex(config.widget.currentIndex()+1)

# checks if combo box is at first index
def first_box(user,label):
	if(isDigit(user) == False):
		label.setText("Invalid*")
		return 0;
	label.setText("")
	return 1;

# clears all numbers from combo boxes, goes to first index(parameter name)
def clear_box(user, label):
	for i in range(0,len(user)):
		user[i].setCurrentIndex(0)
		label[i].setText("")

# updates textbox which represents current values based on combo box input
def update_current(user, current, label):
	for i in range(0,len(user)):
		if(first_box(user[i],label[i])):
			current[i].setText(user[i])	
