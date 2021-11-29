from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
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
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button   
mySerial = comms.serialThreadClass()
# plt.style.use('fivethirtyeight')
va = [0]
xv = [0]

aa = [0]
xa = [0]
indexV = count()
indexA = count()


class graphs_page(QDialog):

    def __init__(self):
        super(graphs_page, self).__init__()
        loadUi("interface/graphs_v2.ui", self)
        self.Back.clicked.connect(self.go_to_menu)
        self.ventricle_view.clicked.connect(self.graph_vent)
        self.atrial_view.clicked.connect(self.graph_atrial)
        self.start_both.clicked.connect(self.graph_both)
        mySerial.open_serial()

    def go_to_menu(self):

        global va,xv,aa,xa,indexV,indexA
        va = [0]
        xv = [0]
        aa = [0]
        xa = [0]
        indexV = count()
        indexA = count()
        mySerial.stop_graph()
        mySerial.close_serial()
        menu_var = menu.main_menu()
        go_to_page(menu_var)


    def get_data(self):
        data = []
        try:
            data1 = mySerial.get_graph()
            atr = data1[0]
            vtr = data1[1]
            return [atr,vtr]
        except:
            print("recieved fail")
            return [data,data]   
        return [data,data]


    def graph_vent(self):
        global mode
        mode = 1
        self.run()

    def graph_atrial(self):
        global mode
        mode = 2
        self.run()

    def graph_both(self):
        global mode
        mode = 3
        self.run()


    def animate(self,i):
        global xv,va,xa,aa
        if(mySerial.read_3()):
            if(mode ==1):

                data = self.get_data()
                temp1 = len(va)
                va = va+data[1]
                temp2 = len(va)
                if(temp1<temp2):
                    for i in range(xv[-1],xv[-1]+9):
                        xv.append(i)

                    # xv.append(next(indexV))
                # print("X: ",xv)
                # print("VA: ",va)
                
                return plt.plot(xv,va,'b-'),

            elif(mode ==2):
                data = self.get_data()
                temp1 = len(aa)
                aa = aa+data[0]
                temp2 = len(aa)

                if(temp1<temp2):
                    for i in range(xa[-1],xa[-1]+3):
                        xa.append(i)

                # print("X: ",xa)
                # print("AA: ",aa)

                return plt.plot(xa,aa,'r-'),
        else:
            if(mode == 1):
                return plt.plot(xv,va,'b-'),
            elif(mode ==2):
                return plt.plot(xa,aa,'r-'), 
            elif(mode == 3):
                plt.plot(xv,va, label='Ventricle')
                return plt.plot(xa,aa, label='Atrial')
            print("failed to animate")


    def run(self):
        mySerial.clear_buff()
        if(mySerial.start_3()):
            fig = plt.figure()
            ani = FuncAnimation(fig,func=self.animate, interval=1000)
            plt.show()
            print("vent")
        else:
            if(mode == 1):
                return plt.plot(xv,va,'b-'),
            elif(mode ==2):
                return plt.plot(xa,aa,'r-'), 
            elif(mode == 3):
                plt.plot(xv,va, label='Ventricle')
                return plt.plot(xa,aa, label='Atrial')
            print("failed to animate")            
















    # def animate(self,i):
    #     global xv,va,xa,aa

    #     if(mode ==1):
    #         data = self.get_data()
    #         temp1 = len(va)
    #         va = va+data[1]
    #         temp2 = len(va)
    #         if(temp1<temp2):
    #             xv.append(next(indexV))
            
    #         print("X: ",xv)
    #         print("VA: ",va)
            
    #         return plt.plot(xv,va,'b-'),

    #     elif(mode ==2):
    #         data = self.get_data()
    #         temp1 = len(aa)
    #         aa = aa+data[0]
    #         temp2 = len(aa)

    #         if(temp1<temp2):
    #             xa.append(next(indexA))

    #         print("X: ",xa)
    #         print("AA: ",aa)

    #         return plt.plot(xa,aa,'r-'),

    # def run(self):
    #     mySerial.clear_buff()
    #     if(mySerial.send_3()):
    #         fig = plt.figure()
    #         ani = FuncAnimation(fig,func=self.animate, interval=1000)
    #         plt.show()
    #         print("vent")
    #     else:
    #         if(mode == 1):
    #             plt.plot(xv,va)
    #             plt.show()
    #         elif(mode ==2):
    #             plt.plot(xa,aa)
    #             plt.show()  
    #         elif(mode == 3):
    #             plt.plot(xv,va, label='Ventricle')
    #             plt.plot(xa,aa, label='Atrial')
    #             plt.legend(loc='upper left')
    #             plt.show()
    #         print("failed to animate")

