# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Changeurtype = QtWidgets.QLabel(self.centralwidget)
        self.Changeurtype.setGeometry(QtCore.QRect(0, 0, 541, 141))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Changeurtype.setFont(font)
        self.Changeurtype.setObjectName("Changeurtype")
        self.Duo = QtWidgets.QRadioButton(self.centralwidget)
        self.Duo.setEnabled(True)
        self.Duo.setChecked(True)
        self.Duo.setGeometry(QtCore.QRect(50, 140, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Duo.setFont(font)
        self.Duo.setObjectName("Duo")
        self.Swimming = QtWidgets.QRadioButton(self.centralwidget)
        self.Swimming.setGeometry(QtCore.QRect(50, 230, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Swimming.setFont(font)
        self.Swimming.setObjectName("Swimming")
        self.RB = QtWidgets.QRadioButton(self.centralwidget)
        self.RB.setGeometry(QtCore.QRect(50, 310, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.RB.setFont(font)
        self.RB.setObjectName("RB")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(820, 600, 191, 111))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Next.setFont(font)
        self.Next.setObjectName("Next")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Changeurtype.setText(_translate("MainWindow", "Выберите тип соревнований:"))
        self.Duo.setText(_translate("MainWindow", "Двоеборие"))
        self.Swimming.setText(_translate("MainWindow", "Плаванье"))
        self.RB.setText(_translate("MainWindow", "Рукопашный бой"))
        self.Next.setText(_translate("MainWindow", "Далее"))
    def add_functions(self):
        self.Next.clicked.connect(self.SecWind)

    def SecWind(self):
        self.Changeurtype.setVisible(False)
        self.Duo.setVisible(False)
        self.Swimming.setVisible(False)
        self.RB.setVisible(False)
        self.Next.setVisible(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())