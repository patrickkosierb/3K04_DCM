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
def first_box(user,current,label,i):
	if(isDigit(user[i]) == False):
		label[i].setText("Invalid*")
		return 0;	
	# elif(isDigit(user[0]) and isDigit(user[1])):
	# 	if(i==0  and  (float(user[0])>float(user[1]) or float(user[0])>float(current[1].text()))):
	# 		label[0].setText("Invalid*")
	# 		return 0;
	# 	else:
	# 		label[i].setText("")
	# elif(isDigit(user[1])):
	# 	if(i==1  and  float(user[1])<float(current[0].text())):
	# 		label[1].setText("Invalid*")
	# 		return 0;
	# elif(isDigit(user[0])):		
	# 	if(i==0  and  float(user[0])>float(current[1].text())):
	# 		label[0].setText("Invalid*")
	# 		return 0;
	else:	
		label[i].setText("")
	return 1;


# clears all numbers from combo boxes, goes to first index(parameter name)
def clear_box(user, label):
	for i in range(0,len(user)):
		user[i].setCurrentIndex(0)
		label[i].setText("")

# updates textbox which represents current values based on combo box input
def update_current(user, current, label):
	print(user)
	for i in range(0,len(user)):
		if(first_box(user,current,label,i)):
			current[i].setText(user[i])	
