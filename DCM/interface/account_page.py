# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1180, 814)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(-130, -10, 1431, 831))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(0, 85, 9, 255), stop:1 rgba(255, 147, 147, 255));}")
        self.bgwidget.setObjectName("bgwidget")
        self.label1 = QtWidgets.QLabel(self.bgwidget)
        self.label1.setGeometry(QtCore.QRect(440, 100, 361, 111))
        self.label1.setStyleSheet("font: 28pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label1.setObjectName("label1")
        self.changes = QtWidgets.QPushButton(self.bgwidget)
        self.changes.setGeometry(QtCore.QRect(640, 570, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.changes.setFont(font)
        self.changes.setStyleSheet("border-radius: 20px;\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(255, 255, 216);\n"
"font: 12pt \"Arial\";")
        self.changes.setObjectName("changes")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(510, 190, 60, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.bgwidget)
        self.label2.setGeometry(QtCore.QRect(420, 220, 181, 21))
        self.label2.setStyleSheet("font: 18pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label2.setObjectName("label2")
        self.label2_2 = QtWidgets.QLabel(self.bgwidget)
        self.label2_2.setGeometry(QtCore.QRect(440, 260, 141, 21))
        self.label2_2.setStyleSheet("font: 14pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label2_2.setObjectName("label2_2")
        self.label2_4 = QtWidgets.QLabel(self.bgwidget)
        self.label2_4.setGeometry(QtCore.QRect(440, 300, 211, 21))
        self.label2_4.setStyleSheet("font: 14pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label2_4.setObjectName("label2_4")
        self.label2_5 = QtWidgets.QLabel(self.bgwidget)
        self.label2_5.setGeometry(QtCore.QRect(420, 370, 141, 31))
        self.label2_5.setStyleSheet("font: 18pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label2_5.setObjectName("label2_5")
        self.label2_6 = QtWidgets.QLabel(self.bgwidget)
        self.label2_6.setGeometry(QtCore.QRect(440, 420, 161, 21))
        self.label2_6.setStyleSheet("font: 14pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label2_6.setObjectName("label2_6")
        self.label2_7 = QtWidgets.QLabel(self.bgwidget)
        self.label2_7.setGeometry(QtCore.QRect(440, 460, 141, 21))
        self.label2_7.setStyleSheet("font: 14pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label2_7.setObjectName("label2_7")
        self.label2_8 = QtWidgets.QLabel(self.bgwidget)
        self.label2_8.setGeometry(QtCore.QRect(440, 500, 191, 21))
        self.label2_8.setStyleSheet("font: 14pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.label2_8.setObjectName("label2_8")
        self.username_new = QtWidgets.QLineEdit(self.bgwidget)
        self.username_new.setGeometry(QtCore.QRect(640, 420, 161, 21))
        self.username_new.setObjectName("username_new")
        self.password = QtWidgets.QLineEdit(self.bgwidget)
        self.password.setGeometry(QtCore.QRect(640, 460, 161, 21))
        self.password.setObjectName("password")
        self.password_confirm = QtWidgets.QLineEdit(self.bgwidget)
        self.password_confirm.setGeometry(QtCore.QRect(640, 500, 161, 21))
        self.password_confirm.setObjectName("password_confirm")
        self.back = QtWidgets.QPushButton(self.bgwidget)
        self.back.setGeometry(QtCore.QRect(640, 620, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.back.setFont(font)
        self.back.setStyleSheet("border-radius: 20px;\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(255, 216, 216);\n"
"font: 12pt \"Arial\";")
        self.back.setObjectName("back")
        self.checkBox = QtWidgets.QCheckBox(self.bgwidget)
        self.checkBox.setGeometry(QtCore.QRect(585, 540, 241, 20))
        self.checkBox.setStyleSheet("font: 8pt \"Arial\"; color:rgb(255,255,255)\n"
"")
        self.checkBox.setObjectName("checkBox")
        self.pm_no = QtWidgets.QLabel(self.bgwidget)
        self.pm_no.setGeometry(QtCore.QRect(640, 290, 181, 41))
        self.pm_no.setStyleSheet("font: 12pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.pm_no.setText("")
        self.pm_no.setObjectName("pm_no")
        self.username = QtWidgets.QLabel(self.bgwidget)
        self.username.setGeometry(QtCore.QRect(640, 250, 181, 41))
        self.username.setStyleSheet("font: 12pt \"Arial\"; color:rgb(255, 255, 255)\n"
"")
        self.username.setText("")
        self.username.setObjectName("username")
        self.invalid_up2 = QtWidgets.QLabel(self.bgwidget)
        self.invalid_up2.setGeometry(QtCore.QRect(630, 520, 181, 31))
        self.invalid_up2.setStyleSheet("font: 8pt \"Arial\"; color:rgb(255, 0, 0)\n"
"")
        self.invalid_up2.setText("")
        self.invalid_up2.setObjectName("invalid_up2")
        self.invalid_up3 = QtWidgets.QLabel(self.bgwidget)
        self.invalid_up3.setGeometry(QtCore.QRect(630, 520, 181, 31))
        self.invalid_up3.setStyleSheet("font: 8pt \"Arial\"; color:rgb(0, 255, 0)\n"
"")
        self.invalid_up3.setText("")
        self.invalid_up3.setObjectName("invalid_up3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label1.setText(_translate("Dialog", "Account Settings"))
        self.changes.setText(_translate("Dialog", "Apply Changes"))
        self.label2.setText(_translate("Dialog", "Account Info"))
        self.label2_2.setText(_translate("Dialog", "Username"))
        self.label2_4.setText(_translate("Dialog", "Pacemaker No."))
        self.label2_5.setText(_translate("Dialog", "Change"))
        self.label2_6.setText(_translate("Dialog", "New Username"))
        self.label2_7.setText(_translate("Dialog", "Password"))
        self.label2_8.setText(_translate("Dialog", "Confirm Password"))
        self.back.setText(_translate("Dialog", "Back to Menu"))
        self.checkBox.setText(_translate("Dialog", "I have reviewed the changes made"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
