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
import devices
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
mySerial = comms.serialThreadClass()
myDevice = devices.Device()

va = [0]
xv = [0]
aa = [0]
xa = [0]

class graphs_page(QDialog):

    def __init__(self):
        super(graphs_page, self).__init__()
        loadUi("interface/graphs_v2.ui", self)
        self.Back.clicked.connect(self.go_to_menu)
        self.ventricle_view.clicked.connect(self.graph_vent)
        self.atrial_view.clicked.connect(self.graph_atrial)
        self.start_both.clicked.connect(self.graph_both)
        self.freeze.clicked.connect(self.plot_freeze)
        self.reset.clicked.connect(self.reset_data)
        self.user_display.setText("User: "+config.is_current_user())
        self.update_patient()

    def go_to_menu(self):

        global va,xv,aa,xa
        va = [0]
        xv = [0]
        aa = [0]
        xa = [0]
        mySerial.stop_graph()
        mySerial.close_serial()
        menu_var = menu.main_menu()
        go_to_page(menu_var)

    def update_patient(self):
        if(myDevice.get_PM()[0]==0):
            print("Not a past device.")
            text, result = QInputDialog.getText(self,"New PM", "Enter new patient's name:")
            if(result == True):
                myDevice.add_device(str(text))
                cur = myDevice.get_PM()
                self.pacemaker_number.setText("Patient: "+cur[0])
                config.current_pm(cur[1])
                if(mySerial.isopen()==0):
                    mySerial.open_serial()
                self.connected.setText("Connected")
                self.disconnected.setText("")
        else:
            cur = myDevice.get_PM()
            self.pacemaker_number.setText("Patient: "+cur[0])
            if(int(cur[1]) == 2):
                self.connected.setText("")
                self.disconnected.setText("Disconnected")
                mySerial.close_serial()
            else:
                if(not mySerial.isopen()):
                    mySerial.open_serial()
                mySerial.close_serial()
                mySerial.open_serial()
                self.connected.setText("Connected")
                self.disconnected.setText("")
            config.current_pm(cur[1])

    def graph_vent(self):
        self.update_patient()
        global mode
        mode = 1
        self.run()

    def graph_atrial(self):
        self.update_patient()
        global mode
        mode = 2
        self.run()

    def graph_both(self):
        self.update_patient()
        global mode
        mode = 3
        self.run()


    def animate(self,i):
        global xv,va,xa,aa

        if(mode == 1):
            data = mySerial.get_graph()
            va = va+data[1]
            for i in range(xv[-1],xv[-1]+len(data[1])):
                xv.append(i)
            return plt.plot(xv,va,'b-',label='Ventricle'),

        elif(mode ==2):
            data = mySerial.get_graph()
            aa = aa+data[0]
            for i in range(xa[-1],xa[-1]+len(data[0])):
                xa.append(i)
            return plt.plot(xa,aa,'r-',label='Atrial'),

        elif(mode == 3):
            data = mySerial.get_graph()
            va = va+data[1]
            aa = aa+data[0]
            for i in range(xv[-1],xv[-1]+len(data[1])):
                xv.append(i)
            for i in range(xa[-1],xa[-1]+len(data[0])):
                xa.append(i)
            plt.plot(xa,aa,'r-',label='Atrial')
            return plt.plot(xv,va,'b-',label='Ventricle'),

    def run(self):
        mySerial.clear_buff()
        if(mySerial.start_3()):
            fig = plt.figure()
            ani = FuncAnimation(fig,func=self.animate, interval=1000)
            plt.show()
            



    def plot_freeze(self):
        mySerial.stop_graph()
        plt.cla()
        plt.plot(xv,va, label='Ventricle')
        plt.plot(xa,aa, label='Atrial')
        plt.legend(loc = 'lower right')
        plt.show()

    def reset_data(self):
        mySerial.stop_graph()
        global va,xv,aa,xa
        va = [0]
        xv = [0]
        aa = [0]
        xa = [0]


