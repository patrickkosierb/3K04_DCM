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
import struct

from itertools import count
import random
# import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

mySerial = comms.serialThreadClass()
# plt.style.use('fivethirtyeight')
x = []
y = []

index = count()
# mySerial.close_serial()

# Width = 2
# va = linspace(0,0,Width)
# x_vent = 0

# aa = linspace(0,0,Width)
# x_atr = 0

# vtr_on = 0
# atr_on = 0

# v_flag = 0
# a_flag = 0

# data = [0, 0]

# mySerial.open_serial()



def animate(i):
    try:
        data = mySerial.get_graph()
        x.append(next(index))
        y.append(data[1])
        print(x)
        print(y)
        plt.cla()
        plt.plot(x,y)
    except struct.error:
        # mySerial.close_serial()
        plt.close()
        print("values not received")
        # return 0


# def get_data(void):


class graphs_page(QDialog):

    def __init__(self):
        super(graphs_page, self).__init__()
        loadUi("interface/graphs.ui", self)
        self.Back.clicked.connect(self.go_to_menu)
        self.ventricle_view.clicked.connect(self.graph_vent)
        # self.stop_vent.clicked.connect(self.stop_graph_vent)
        self.atrial_view.clicked.connect(self.graph_atrial)
        # self.vent = self.vent_graph.plot()
        # self.atr = self.atr_graph.plot()


    def go_to_menu(self):
        # global x_vent,va,v_flag,v_on,x_atr,aa,a_flag,atr_on

        # v_flag = 0
        # va = linspace(0,0,Width)
        # x_vent = 0
        # v_on = 0

        # a_flag = 0
        # aa = linspace(0,0,Width)
        # x_atr = 0
        # a_on = 0

        # self.vent_graph.plot()
        # self.atr_graph.plot()
        # mySerial.open_serial()
        # mySerial.stop_graph()
        # mySerial.close_serial()
        menu_var = menu.main_menu()
        go_to_page(menu_var)



    def graph_vent(self):

        if(mySerial.send_3()):
            ani = FuncAnimation(plt.gcf(),animate, interval=2000)
            plt.show()
            print("vent")
        else:
            print("failed to animate")

    def graph_atrial(self):
        print("atr")





    # def graph_vent(self):

    #     mySerial.open_serial()
    #     global v_flag,data, x_vent, va, vtr_on
    #     v_flag = 1
    #     if(atr_on==0):
    #         vtr_on = 1
    #         if(mySerial.send_3()):

    #             while v_flag:
    #                 va[:-1] = va[1:]
    #                 try:
    #                     data = mySerial.get_graph()
    #                     va[-1] = data[1]

    #                 except struct.error:
    #                     v_flag = 0
    #                     print("values not received")
    #                     mySerial.close_serial()
    #                     break
    #                 x_vent +=0.1
    #                 self.vent.setData(va)
    #                 self.vent.setPos(x_vent,0)
    #                 QtGui.QApplication.processEvents()

    #         else:
    #             mySerial.close_serial()
        
    #     else:
    #         while v_flag:
    #             va[:-1] = va[1:]
    #             va[-1] = data[1]
    #             x_vent +=0.0001
    #             self.vent.setData(va)
    #             self.vent.setPos(x_vent,0)
    #             QtGui.QApplication.processEvents()



    # def graph_atrial(self):
    #     # value = 1
    #     global a_flag,data, x_atr, aa, atr_on
    #     a_flag = 1
    #     if(vtr_on==0):
    #         atr_on = 1

    #         if(mySerial.send_3()):

    #             while a_flag:
    #                 aa[:-1] = aa[1:]
    #                 try:
    #                     data = mySerial.get_graph()
    #                     aa[-1] = data[0]
    #                 except struct.error:
    #                     a_flag = 0
    #                     print("values not received")
    #                     break
    #                 x_atr +=0.0001
    #                 self.atr.setData(aa)
    #                 self.atr.setPos(x_atr,0)
    #                 QtGui.QApplication.processEvents()
                
    #     else:
    #         atr_on = 1
    #         while a_flag:
    #             aa[:-1] = aa[1:]
    #             aa[-1] = data[0]
    #             x_atr +=0.0001
    #             self.atr.setData(aa)
    #             self.atr.setPos(x_atr,0)
    #             QtGui.QApplication.processEvents()


    # def stop_graph_vent(self):
    #     global v_flag,vtr_on
    #     vtr_on = 0
    #     v_flag = 0
    #     self.vent_graph.plot()
    #     mySerial.close_serial()

    # def stop_graph_atr(self):
    #     global a_flag,atr_on
    #     atr_on = 0
    #     a_flag = 0
    #     self.atr_graph.plot()
