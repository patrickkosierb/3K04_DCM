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
def isValid(user,current,label,i):

	if(isDigit(user[i]) == False):
		# label[i].setText("Invalid*")
		return 0;	
	else:	
		label[i].setText("")
	return 1;


# updates textbox which represents current values based on combo box input
def update_current(user, current, label):
	for i in range(0,len(user)):
		if(isValid(user,current,label,i)):
			current[i].setText(user[i])	

def load_current():
	# cur = config.is_current_pm()
	# try:
	db = open("data/parameters.txt","r")
	for line in db:
		last_line = line
	last_param = last_line.split(", ")
	last_param.pop()
	db.close()
	# except:
	# 	db = open("data/PM-ID-"+cur+".txt","w+")
	# 	db.write("0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ")
	# 	db.close()
	# 	last_param = ['0', '0', '0', '0','0', '0', '0','0', '0', '0', '0','0', '0', '0', '0']
	return last_param

def update_text(param):
	# cur = config.is_current_pm()
	db = open("data/parameters.txt","a")
	db.write("\n")
	for val in param:
		db.write(""+val+", ")
	db.close()


# clears all numbers from combo boxes, goes to first index(parameter name)
def clear_box(user, label):
	for i in range(0,len(user)):
		user[i].setCurrentIndex(0)
		label[i].setText("")
