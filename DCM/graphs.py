from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

import sys
import os
import string

import config
import menu
from helpers import go_to_page

class graphs_page(QDialog): 
    def __init__(self):
        super(graphs_page, self).__init__()
        loadUi("interface/graphs.ui", self)
        self.ventricle_graph = pg.PlotWidget()
        self.atrial_graph = pg.PlotWidget()
        self.Back.clicked.connect(self.go_to_menu)
        self.ventricle_view.clicked.connect(self.graph_vent)
        self.atrial_view.clicked.connect(self.graph_atrial)


    def go_to_menu(self):
    	menu_var = menu.main_menu()
    	go_to_page(menu_var)

    def graph_vent(self):
    	print("vent")
    	# x = [1,2,3,4,5,6]
    	# y = [1,2,3,4,5,6]
    	# pen = pg.mkPen(color=(255,0,0))
    	# self.ventricle_graph.plot(x,y,pen=pen)

    def graph_atrial(self):
    	print("atrial")