# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ThirdWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AddPlayer = QtWidgets.QPushButton(self.centralwidget)
        self.AddPlayer.setGeometry(QtCore.QRect(40, 50, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.AddPlayer.setFont(font)
        self.AddPlayer.setObjectName("AddPlayer")
        self.EditPlayer = QtWidgets.QPushButton(self.centralwidget)
        self.EditPlayer.setGeometry(QtCore.QRect(40, 170, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.EditPlayer.setFont(font)
        self.EditPlayer.setObjectName("EditPlayer")
        self.DelPlayer = QtWidgets.QPushButton(self.centralwidget)
        self.DelPlayer.setGeometry(QtCore.QRect(40, 290, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.DelPlayer.setFont(font)
        self.DelPlayer.setObjectName("DelPlayer")
        self.Back2 = QtWidgets.QPushButton(self.centralwidget)
        self.Back2.setGeometry(QtCore.QRect(40, 430, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Back2.setFont(font)
        self.Back2.setObjectName("Back2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AddPlayer.setText(_translate("MainWindow", "Добавить участника"))
        self.EditPlayer.setText(_translate("MainWindow", "Редактировать участника"))
        self.DelPlayer.setText(_translate("MainWindow", "Удалить участника"))
        self.Back2.setText(_translate("MainWindow", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())