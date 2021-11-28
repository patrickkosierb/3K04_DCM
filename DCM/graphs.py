from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from pyqtgraph import PlotWidget
from pyqtgraph.Qt import QtGui, QtCore
from  numpy import * 

import sys
import os
import string
import time
import config
import menu
from helpers import go_to_page
import comms

mySerial = comms.serialThreadClass()

Width = 2
Xm = linspace(0,0,Width)
print(Xm)
ptr = 0
flag = 0

class graphs_page(QDialog):

    def __init__(self):
        super(graphs_page, self).__init__()
        loadUi("interface/graphs.ui", self)
        self.Back.clicked.connect(self.go_to_menu)
        self.ventricle_view.clicked.connect(self.graph_vent)
        self.atrial_view.clicked.connect(self.graph_atrial)
        self.vent = self.vent_graph.plot()
        # self.flag = 1

    def get_data(self):
        # self.flag = 0
        mySerial.open_serial()
        atr, vent = mySerial.get_graph()
        mySerial.close_serial()
        return atr, vent

    def go_to_menu(self):


        global ptr,Xm, flag
        flag = 0
        Width = 2
        Xm = linspace(0,0,Width)
        ptr = 0
        self.vent = self.vent_graph.plot()
       
        mySerial.open_serial()
        mySerial.stop_graph()
        mySerial.close_serial()
        
        menu_var = menu.main_menu()
        go_to_page(menu_var)
        # self.vent.clear()

    def graph_vent(self):
        value = 1
        global flag
        flag = 1
        while flag:
            global ptr, Xm
            Xm[:-1] = Xm[1:]
            Xm[-1] = value
       
            # value = value +1
            ptr +=0.0001
            self.vent.setData(Xm)
            self.vent.setPos(ptr,0)
            QtGui.QApplication.processEvents()

    def graph_atrial(self):
        x = np.random.normal(size=1000)
        y = np.random.normal(size = (3,1000))
        for i in range(3):
            self.atr_graph.plot(x,y[i],pen=(i,3))


    # def stop_vent(self):

    # def stop_atrial(self):

# def update():
#     global ptr, Xm
#     Xm[:-1] = Xm[1:]
#     Xm[-1] = value
#     value = value +1
#     ptr +=1
#     self.vent.setData(Xm)
#     self.vent.setPos(ptr,0)


