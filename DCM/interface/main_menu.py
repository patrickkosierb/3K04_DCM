# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(0, 85, 9, 255), stop:1 rgba(255, 147, 147, 255));}")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(20, -20, 261, 111))
        self.label.setStyleSheet("font: 20pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label.setObjectName("label")
        self.modes = QtWidgets.QPushButton(self.bgwidget)
        self.modes.setGeometry(QtCore.QRect(10, 170, 351, 51))
        self.modes.setStyleSheet("border-radius: 20px;\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(255, 255, 216);\n"
"font: 12pt \"Arial\";")
        self.modes.setObjectName("modes")
        self.line_2 = QtWidgets.QFrame(self.bgwidget)
        self.line_2.setGeometry(QtCore.QRect(370, -10, 21, 861))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Main Menu"))
        self.modes.setText(_translate("Dialog", "Modes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
