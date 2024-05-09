from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QLabel, QLineEdit, QVBoxLayout, QComboBox, QPushButton, QMessageBox, QWidget
from functools import partial
import os


'''class AddTeamDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить команду")
        self.resize(700, 300)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)

        layout = QVBoxLayout()

        label = QLabel("Введите название команды:")
        self.textEdit = QLineEdit()

        button = QPushButton("Добавить")
        button.clicked.connect(self.accept)

        layout.addWidget(label)
        layout.addWidget(self.textEdit)
        layout.addWidget(button)

        self.setLayout(layout)
        self.show() '''

class AddTeamDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить команду")
        self.resize(700, 300)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)

        layout = QVBoxLayout()

        label = QLabel("Введите название команды:")
        self.textEdit = QLineEdit()

        button = QPushButton("Добавить")
        button.clicked.connect(self.add_command)  # Changed the signal connection

        layout.addWidget(label)
        layout.addWidget(self.textEdit)
        layout.addWidget(button)

        self.setLayout(layout)
        self.show()

    # Added a new method to handle adding the command
    '''def add_command(self):
        team_name = self.textEdit.text()
        with open("commands.txt", "a") as file:
            file.write(team_name + "\n")'''

    '''def add_command(self):
        team_name = self.textEdit.text()
        with open("commands.txt", "r") as file:
            commands = file.readlines()
            if team_name + '\n' in commands:
                QMessageBox.critical(self, 'Ошибка', 'Такая команда уже есть в списках.')
            else:
                with open("commands.txt", "a") as file:
                    file.write(team_name + "\n")
                QMessageBox.information(self, 'Успешно', 'Команда успешно добавлена.')'''

    def add_command(self):
        team_name = self.textEdit.text()
        with open("commands.txt", "r") as file:
            commands = file.readlines()
            if team_name + '\n' in commands:
                QMessageBox.critical(self, 'Ошибка', 'Такая команда уже есть в списках.')
            else:
                with open("commands.txt", "a") as file:
                    if commands[-1] == '\n':  # Проверяем наличие пустой строки в конце
                        file.seek(-1, os.SEEK_END)  # Перемещаем указатель перед последним символом
                        file.truncate()  # Удаляем пустую строку
                    file.write(team_name + "\n")
                QMessageBox.information(self, 'Успешно', 'Команда успешно добавлена.')


class EditTeamDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Редактировать команду")
        self.resize(700, 300)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)

        layout = QVBoxLayout()

        label = QLabel("Введите название команды:")
        self.textEdit = QLineEdit()

        button = QPushButton("Проверить наличие в списке команд")
        button.clicked.connect(self.accept)

        layout.addWidget(label)
        layout.addWidget(self.textEdit)
        layout.addWidget(button)

        self.setLayout(layout)
        self.show()

class DelTeamDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Удалить команду")
        self.resize(700, 300)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)

        layout = QVBoxLayout()

        label = QLabel("Введите название команды:")
        self.textEdit = QLineEdit()

        button = QPushButton("Удалить команду")
        button.clicked.connect(self.accept)


        layout.addWidget(label)
        layout.addWidget(self.textEdit)
        layout.addWidget(button)

        self.setLayout(layout)
        self.show()

'''class CommandWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Command List')

        layout = QVBoxLayout()

        self.setLayout(layout)

        command_window = QMessageBox()
        command_window.setWindowTitle('Command List')

        with open("commands.txt", "r") as file:
            commands = [line.strip() for line in file.readlines()]

        command_combo = QComboBox()
        command_combo.addItems(commands)

        command_window.layout().addWidget(command_combo)
        command_window.exec_()'''

class CommandWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Command List')
        layout = QVBoxLayout()
        self.setLayout(layout)

        command_window = QWidget()
        command_window.setWindowTitle('Command List')
        command_window_layout = QVBoxLayout()
        command_window.setLayout(command_window_layout)

        with open("commands.txt", "r") as file:
            commands = [line.strip() for line in file.readlines()]

        command_label = QLabel("Список команд:")
        command_combo = QComboBox()
        command_combo.addItems(commands)

        command_window_layout.addWidget(command_label)
        command_window_layout.addWidget(command_combo)

        layout.addWidget(command_window)
        self.show()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(40, 590, 211, 121))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Back.setFont(font)
        self.Back.setObjectName("Back")
        self.Back.setVisible(False)
        self.UrChange = QtWidgets.QLabel(self.centralwidget)
        self.UrChange.setGeometry(QtCore.QRect(40, 20, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.UrChange.setFont(font)
        self.UrChange.setObjectName("UrChange")
        self.UrChange.setVisible(False)
        self.AddTeam = QtWidgets.QPushButton(self.centralwidget)
        self.AddTeam.setGeometry(QtCore.QRect(40, 100, 301, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.AddTeam.setFont(font)
        self.AddTeam.setObjectName("AddTeam")
        self.AddTeam.setVisible(False)
        self.EditTeam = QtWidgets.QPushButton(self.centralwidget)
        self.EditTeam.setGeometry(QtCore.QRect(40, 230, 341, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.EditTeam.setFont(font)
        self.EditTeam.setObjectName("EditTeam")
        self.EditTeam.setVisible(False)
        self.DeleteTeam = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteTeam.setGeometry(QtCore.QRect(40, 360, 311, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteTeam.setFont(font)
        self.DeleteTeam.setObjectName("DeleteTeam")
        self.DeleteTeam.setVisible(False)
        self.Changeurtype = QtWidgets.QLabel(self.centralwidget)
        self.Changeurtype.setGeometry(QtCore.QRect(40, 20, 511, 51))
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
        self.Commands = QtWidgets.QPushButton(self.centralwidget)
        self.Commands.setGeometry(QtCore.QRect(640, 100, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Commands.setVisible(False)
        self.Commands.setFont(font)
        self.Commands.setObjectName("Commands")
        self.Players = QtWidgets.QPushButton(self.centralwidget)
        self.Players.setGeometry(QtCore.QRect(640, 360, 411, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Players.setVisible(False)
        self.Players.setFont(font)
        self.Players.setObjectName("Players")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Back.setText(_translate("MainWindow", "Назад"))
        self.AddTeam.setText(_translate("MainWindow", "Добавить команду"))
        self.EditTeam.setText(_translate("MainWindow", "Редактировать команду"))
        self.DeleteTeam.setText(_translate("MainWindow", "Удалить команду"))
        self.Changeurtype.setText(_translate("MainWindow", "Выберите тип соревнований:"))
        self.Duo.setText(_translate("MainWindow", "Двоеборие"))
        self.Swimming.setText(_translate("MainWindow", "Плаванье"))
        self.RB.setText(_translate("MainWindow", "Рукопашный бой"))
        self.Next.setText(_translate("MainWindow", "Далее"))
        self.Commands.setText(_translate("MainWindow", "Вывести список команд"))
        self.Players.setText(_translate("MainWindow", "Вывести список участников"))
    def add_functions(self):
        self.Next.clicked.connect(self.SecWind)
        self.Back.clicked.connect(self.FirstWind)
        self.AddTeam.clicked.connect(self.openAddTeamDialog)
        self.EditTeam.clicked.connect(self.openEditTeamDialog)
        self.DeleteTeam.clicked.connect(self.openDelTeamDialog)
        self.Commands.clicked.connect(self.ShowCommands)   # Создаем экземпляр ShowCommands и вызываем его

        '''self.Players.clicked.connect(self.ShowPlayers)'''

    def SecWind(self):
        self.Changeurtype.setVisible(False)
        self.Duo.setVisible(False)
        self.Swimming.setVisible(False)
        self.RB.setVisible(False)
        self.Next.setVisible(False)
        self.Back.setVisible(True)
        self.UrChange.setVisible(True)
        self.AddTeam.setVisible(True)
        self.EditTeam.setVisible(True)
        self.DeleteTeam.setVisible(True)
        self.Players.setVisible(True)
        self.Commands.setVisible(True)
    def FirstWind(self):
        self.Changeurtype.setVisible(True)
        self.Duo.setVisible(True)
        self.Swimming.setVisible(True)
        self.RB.setVisible(True)
        self.Next.setVisible(True)
        self.Back.setVisible(False)
        self.UrChange.setVisible(False)
        self.AddTeam.setVisible(False)
        self.EditTeam.setVisible(False)
        self.DeleteTeam.setVisible(False)
        self.Players.setVisible(False)
        self.Commands.setVisible(False)

    def openAddTeamDialog(self):
        dialog = AddTeamDialog()
        if dialog.exec_() == QDialog.Accepted:  # Проверяем, было ли добавлено значение
            team_name = dialog.textEdit.text()

    def openEditTeamDialog(self):
        dialog = EditTeamDialog()
        if dialog.exec_() == QDialog.Accepted:
            team_name = dialog.textEdit.text()

    def openDelTeamDialog(self):
        dialog = DelTeamDialog()
        if dialog.exec_() == QDialog.Accepted:
            team_name = dialog.textEdit.text()

    def ShowCommands(self):
        Message = CommandWindow()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
