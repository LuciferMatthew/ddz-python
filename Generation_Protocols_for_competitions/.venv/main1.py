from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QLabel, QLineEdit, QVBoxLayout, QComboBox, QPushButton, QMessageBox
from PyQt5.QtWidgets import QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import QTimer
import os

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
    def add_command(self):
        team_name = self.textEdit.text()
        with open("commands.txt", "a+") as file:
            file.seek(0)  # Переходим в начало файла
            commands = file.readlines()
            if commands and team_name + '\n' in commands:
                QMessageBox.critical(self, 'Ошибка', 'Такая команда уже есть в списках.')
            else:
                if commands and commands[-1].strip() == '':  # Проверяем наличие пустой строки в конце
                    file.seek(-1, os.SEEK_END)  # Перемещаем указатель перед последним символом
                    file.truncate()  # Удаляем пустую строку
                file.write(team_name + "\n")
                QMessageBox.information(self, 'Успешно', 'Команда успешно добавлена.')



class EditTeamDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Редактировать название команды")
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
        button.clicked.connect(self.check_team_name)  # При нажатии кнопки вызываем метод для проверки наличия команды

        layout.addWidget(label)
        layout.addWidget(self.textEdit)
        layout.addWidget(button)

        self.resultLabel = QLabel("")

        # Новый стиль для жирного текста
        self.resultLabel.setStyleSheet("font-weight: bold")

        layout.addWidget(self.resultLabel)

        self.editLabel = QLabel("Введите новое название команды:")
        self.editTextEdit = QLineEdit()

        editButton = QPushButton("Изменить название команды")
        editButton.clicked.connect(self.edit_team_name)

        layout.addWidget(self.editLabel)
        layout.addWidget(self.editTextEdit)
        layout.addWidget(editButton)

        self.setLayout(layout)
        self.show()

    def check_team_name(self):
        team_name = self.textEdit.text()
        found = False
        with open("commands.txt", "r") as file:
            for line in file:
                if team_name.lower() in line.lower():
                    self.resultLabel.setStyleSheet("background-color: green; font-size: 20px;")
                    self.resultLabel.setText("<b>Такая команда есть в списках, вы можете изменить ее название!</b>")
                    found = True
                    break
        if not found:
            self.resultLabel.setStyleSheet("background-color: red; font-size: 20px;")
            self.resultLabel.setText("<b>Такой команды нет в списках.</b>")

    def edit_team_name(self):
        old_name = self.textEdit.text()
        new_name = self.editTextEdit.text()

        with open("commands.txt", "r") as file:
            data = file.readlines()

        with open("commands.txt", "w") as file:
            for line in data:
                if line.strip() == old_name:
                    file.write(new_name + "\n")
                else:
                    file.write(line)

        QMessageBox.information(self, 'Успешно', 'Название команды успешно изменено.')

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

        button = QPushButton("Удалить")
        button.clicked.connect(self.delete_command)  # Соединяем кнопку с методом удаления команды

        layout.addWidget(label)
        layout.addWidget(self.textEdit)
        layout.addWidget(button)

        self.setLayout(layout)
        self.show()

    def delete_command(self):
        team_name = self.textEdit.text()
        found = False
        with open("commands.txt", "r") as file:
            data = file.readlines()

        with open("commands.txt", "w") as file:
            for line in data:
                if line.strip() != team_name:
                    file.write(line)
                else:
                    found = True

        if found:
            QMessageBox.information(self, 'Успешно', 'Команда успешно удалена.')
        else:
            QMessageBox.critical(self, 'Ошибка', 'Команда не найдена.')


class CommandWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Command List')
        layout = QVBoxLayout()
        self.setLayout(layout)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setWeight(75)
        self.setFont(font)

        with open("commands.txt", "r+") as file:
            commands = [line.strip() for line in file.readlines()]

        command_combo = QComboBox()
        command_combo.addItems(commands)
        layout.addWidget(command_combo)
        self.setLayout(layout)
        self.show()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AddPlayer = QtWidgets.QPushButton(self.centralwidget)
        self.AddPlayer.setGeometry(QtCore.QRect(40, 100, 301, 91))
        self.AddPlayer.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.AddPlayer.setFont(font)
        self.AddPlayer.setObjectName("AddPlayer")
        self.EditPlayer = QtWidgets.QPushButton(self.centralwidget)
        self.EditPlayer.setGeometry(QtCore.QRect(40, 230, 341, 91))
        self.EditPlayer.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.EditPlayer.setFont(font)
        self.EditPlayer.setObjectName("EditPlayer")
        self.DelPlayer = QtWidgets.QPushButton(self.centralwidget)
        self.DelPlayer.setGeometry(QtCore.QRect(40, 360, 311, 91))
        self.DelPlayer.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.DelPlayer.setFont(font)
        self.DelPlayer.setObjectName("DelPlayer")
        self.Back2 = QtWidgets.QPushButton(self.centralwidget)
        self.Back2.setGeometry(QtCore.QRect(40, 590, 211, 121))
        self.Back2.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Back2.setFont(font)
        self.Back2.setObjectName("Back2")
        self.Next2 = QtWidgets.QPushButton(self.centralwidget)
        self.Next2.setGeometry(QtCore.QRect(820, 600, 191, 111))
        self.Next2.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Next2.setFont(font)
        self.Next2.setObjectName("Next")
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
        self.command_label = QtWidgets.QLabel(self.centralwidget)
        self.command_label.setGeometry(QtCore.QRect(520, 300, 511, 41))
        font = QtGui.QFont()
        self.command_label.setVisible(False)
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.command_label.setFont(font)
        self.command_label.setObjectName("command_label")
        self.command_label.setText("Список команд:")
        MainWindow.setCentralWidget(self.centralwidget)
        layout = QHBoxLayout(self.centralwidget)

        timer = QTimer(MainWindow)
        timer.timeout.connect(self.updateComboBox)
        timer.start(1000)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setWeight(75)

        self.command_combo = QComboBox()
        self.command_combo.setFont(font)
        self.command_combo.setVisible(False)

        file_path = "commands.txt"
        if not os.path.exists(file_path):
            with open(file_path, "w"):
                pass

        with open(file_path, "r+") as file:
            commands = [line.strip() for line in file.readlines()]

        self.command_combo.addItems(commands)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        layout.addItem(spacer)
        layout.addWidget(self.command_combo, stretch=1)

        self.centralwidget.setLayout(layout)
        MainWindow.setCentralWidget(self.centralwidget)

        # Определяем размеры комбобокса
        combo_width = 532  # половина ширины окна
        combo_height = 50  # высота окна
        self.command_combo.setFixedSize(combo_width, combo_height)

        self.add_functions()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def updateComboBox(self):
        file_path = "commands.txt"
        with open(file_path, "r") as file:
            commands = [line.strip() for line in file.readlines()]

        current_items = [self.command_combo.itemText(i) for i in range(self.command_combo.count())]
        if commands != current_items:
            self.command_combo.clear()
            self.command_combo.addItems(commands)

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
        self.Next2.setText(_translate("MainWindow", "Далее"))
        self.AddPlayer.setText(_translate("MainWindow", "Добавить участника"))
        self.EditPlayer.setText(_translate("MainWindow", "Редактировать участника"))
        self.DelPlayer.setText(_translate("MainWindow", "Удалить участника"))
        self.Back2.setText(_translate("MainWindow", "Назад"))

    def add_functions(self):
        self.Next.clicked.connect(self.SecWind)
        self.Back.clicked.connect(self.FirstWind)
        self.Next2.clicked.connect(self.ThirdWind)
        self.Back2.clicked.connect(self.SecWind)
        self.AddTeam.clicked.connect(self.openAddTeamDialog)
        self.EditTeam.clicked.connect(self.openEditTeamDialog)
        self.DeleteTeam.clicked.connect(self.openDelTeamDialog)

    def ThirdWind(self):
        self.Changeurtype.setVisible(False)
        self.Duo.setVisible(False)
        self.Swimming.setVisible(False)
        self.RB.setVisible(False)
        self.Next.setVisible(False)
        self.Back.setVisible(False)
        self.UrChange.setVisible(False)
        self.AddTeam.setVisible(False)
        self.EditTeam.setVisible(False)
        self.DeleteTeam.setVisible(False)
        self.command_combo.setVisible(False)
        self.command_label.setVisible(False)
        self.Next2.setVisible(False)
        self.AddPlayer.setVisible(True)
        self.EditPlayer.setVisible(True)
        self.DelPlayer.setVisible(True)
        self.Back2.setVisible(True)

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
        self.command_combo.setVisible(True)
        self.command_label.setVisible(True)
        self.Next2.setVisible(True)
        self.AddPlayer.setVisible(False)
        self.EditPlayer.setVisible(False)
        self.DelPlayer.setVisible(False)
        self.Back2.setVisible(False)
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
        self.command_combo.setVisible(False)
        self.command_label.setVisible(False)
        self.Next2.setVisible(False)
        self.AddPlayer.setVisible(False)
        self.EditPlayer.setVisible(False)
        self.DelPlayer.setVisible(False)
        self.Back2.setVisible(False)

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

    def ShowCommandsDialog(self):
        dialog = CommandWindow()
        if dialog.exec_() == QDialog.Accepted:
            team_name = dialog.textEdit.text()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
