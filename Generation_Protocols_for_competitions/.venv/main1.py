from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QLabel, QLineEdit, QVBoxLayout, QComboBox, QPushButton, QMessageBox
from PyQt5.QtWidgets import QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import QTimer, Qt
import os
from Exel import CreateExel

class AddTeamDialog(QDialog):
    def __init__(self):
        super().__init__(None, Qt.Dialog)
        self.setWindowTitle("Добавить команду")
        self.setWindowModality(Qt.ApplicationModal)
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
        button.clicked.connect(self.add_command)

        layout.addWidget(label)
        layout.addWidget(self.textEdit)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_command(self):
        team_name = self.textEdit.text()
        with open("commands.txt", "a+") as file:
            file.seek(0)
            commands = file.readlines()
            if commands and team_name + '\n' in commands:
                QMessageBox.critical(self, 'Ошибка', 'Такая команда уже есть в списках.')
            else:
                if commands and commands[-1].strip() == '':
                    file.seek(-1, os.SEEK_END)
                    file.truncate()
                file.write(team_name + "\n")
                QMessageBox.information(self, 'Успешно', 'Команда успешно добавлена.')
                self.accept()  # Закрываем окно успешно добавленной команды





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

        self.labelComboBox = QLabel("Выберите команду для редактирования:")
        self.command_combo = QComboBox()

        file_path = "commands.txt"
        if not os.path.exists(file_path):
            with open(file_path, "w"):
                pass

        with open(file_path, "r+") as file:
            commands = [line.strip() for line in file.readlines()]

        self.command_combo.addItems(commands)

        layout.addWidget(self.labelComboBox)
        layout.addWidget(self.command_combo)

        timer = QTimer(MainWindow)
        timer.timeout.connect(self.updateComboBox)
        timer.start(1000)

        self.resultLabel = QLabel("")
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

    def edit_team_name(self):
        old_name = self.command_combo.currentText()
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

    def updateComboBox(self):
        file_path = "commands.txt"
        with open(file_path, "r") as file:
            commands = [line.strip() for line in file.readlines()]

        current_items = [self.command_combo.itemText(i) for i in range(self.command_combo.count())]
        if commands != current_items:
            self.command_combo.clear()
            self.command_combo.addItems(commands)




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


class AddPlayerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить участника")
        self.setFixedSize(400, 300)

        self.setAttribute(Qt.WA_DeleteOnClose)

        layout = QtWidgets.QVBoxLayout()

        self.command_combo = QComboBox()

        file_path = "commands.txt"
        if not os.path.exists(file_path):
            with open(file_path, "w"):
                pass

        with open(file_path, "r+") as file:
            commands = [line.strip() for line in file.readlines()]

        self.command_combo.addItems(commands)

        layout.addWidget(self.command_combo)

        self.FIO_edit = QtWidgets.QLineEdit()
        self.FIO_edit.setPlaceholderText("ФИО участника")
        layout.addWidget(self.FIO_edit)



        self.badge_number_edit = QtWidgets.QLineEdit()
        self.badge_number_edit.setPlaceholderText("Нагрудный номер")
        layout.addWidget(self.badge_number_edit)

        radio_layout = QHBoxLayout()
        self.male_rb = QtWidgets.QRadioButton("Мужской")
        self.female_rb = QtWidgets.QRadioButton("Женский")
        radio_layout.addWidget(self.male_rb)
        radio_layout.addWidget(self.female_rb)
        layout.addLayout(radio_layout)

        self.shooting_result_edit = QtWidgets.QLineEdit()
        self.shooting_result_edit.setPlaceholderText("Результат стрельбы")
        layout.addWidget(self.shooting_result_edit)

        self.running_result_edit = QtWidgets.QLineEdit()
        self.running_result_edit.setPlaceholderText("Результат бега")
        layout.addWidget(self.running_result_edit)

        add_button = QtWidgets.QPushButton("Добавить участника")
        add_button.clicked.connect(self.add_player)
        layout.addWidget(add_button)

        self.setLayout(layout)

        # Создание файла "Players.txt", если он не существует
        if not os.path.exists("Players.txt"):
            with open("Players.txt", "w") as file:
                pass

    def add_player(self):
        if self.male_rb.isChecked():
            Gender = 'М'
        else:
            Gender = 'Ж'

        data = f"{self.FIO_edit.text()}_{self.command_combo.currentText()}_{self.badge_number_edit.text()}_{Gender}_{self.shooting_result_edit.text()}_{self.running_result_edit.text()}\n"

        with open("Players.txt", "r") as file:
            lines = file.readlines()
            if any(data in line for line in lines):
                QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Такой игрок уже есть в списках')
            else:
                with open("Players.txt", "a") as file:
                    file.write('\n' + data)
                    QtWidgets.QMessageBox.information(self, 'Успех', 'Игрок успешно добавлен')

class EditPlayerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Редактировать участника")
        self.setFixedSize(400, 250)

        self.setAttribute(Qt.WA_DeleteOnClose)
        layout = QtWidgets.QVBoxLayout()

        label = QLabel("Выберите участника, которого хотите изменить:")
        layout.addWidget(label)

        self.player_combo = QComboBox()
        self.load_players_from_file()
        self.player_combo.currentIndexChanged.connect(self.update_fields)  # Connect signal to update fields

        layout.addWidget(self.player_combo)

        self.command_combo = QComboBox()

        file_path = "commands.txt"
        if not os.path.exists(file_path):
            with open(file_path, "w"):
                pass

        with open(file_path, "r+") as file:
            commands = [line.strip() for line in file.readlines()]

        self.command_combo.addItems(commands)

        layout.addWidget(self.command_combo)

        self.FIO_edit = QtWidgets.QLineEdit()
        self.FIO_edit.setPlaceholderText("ФИО участника")
        layout.addWidget(self.FIO_edit)

        self.badge_number_edit = QtWidgets.QLineEdit()
        self.badge_number_edit.setPlaceholderText("Нагрудный номер")
        layout.addWidget(self.badge_number_edit)

        radio_layout = QHBoxLayout()
        self.male_rb = QtWidgets.QRadioButton("Мужской")
        self.female_rb = QtWidgets.QRadioButton("Женский")
        radio_layout.addWidget(self.male_rb)
        radio_layout.addWidget(self.female_rb)
        layout.addLayout(radio_layout)

        timer = QTimer(self)
        timer.timeout.connect(self.updateComboBox)
        timer.start(1000)

        self.shooting_result_edit = QtWidgets.QLineEdit()
        self.shooting_result_edit.setPlaceholderText("Результат стрельбы")
        layout.addWidget(self.shooting_result_edit)

        self.running_result_edit = QtWidgets.QLineEdit()
        self.running_result_edit.setPlaceholderText("Результат бега")
        layout.addWidget(self.running_result_edit)

        add_button = QtWidgets.QPushButton("Изменить участника")
        add_button.clicked.connect(self.edit_player)
        layout.addWidget(add_button)

        self.setLayout(layout)

        self.load_selected_player_data()

        if not os.path.exists("Players.txt"):
            with open("Players.txt", "w") as file:
                pass

        with open("Players.txt", "r") as file:
            lines = [line.strip() for line in file if line.strip()]

        with open("Players.txt", "w") as file:
            file.writelines('\n'.join(lines))

    def load_selected_player_data(self):
        selected_player = self.player_combo.currentText()
        with open("Players.txt", "r") as file:
            for line in file:
                if selected_player in line:
                    data = line.split('_')
                    self.FIO_edit.setText(data[0])
                    self.command_combo.setCurrentText(data[1])
                    self.badge_number_edit.setText(data[2])
                    gender = data[3]
                    if gender == 'М':
                        self.male_rb.setChecked(True)
                    else:
                        self.female_rb.setChecked(True)
                    self.shooting_result_edit.setText(data[4])
                    self.running_result_edit.setText(data[5])
                    break

    def load_players_from_file(self):
        with open("Players.txt", "r") as file:
            players = [line.split('_')[0].strip() for line in file.readlines() if line.strip()]
            self.player_combo.addItems(players)

    def updateComboBox(self):
        with open("Players.txt", "r") as file:
            players = [line.split('_')[0].strip() for line in file.readlines()]

        current_items = [self.player_combo.itemText(i) for i in range(self.player_combo.count())]

        if set(players) != set(current_items):
            self.player_combo.clear()
            self.player_combo.addItems(players)

    def update_fields(self):
        selected_player = self.player_combo.currentText()
        with open("Players.txt", "r") as file:
            for line in file:
                if selected_player in line:
                    data = line.split('_')
                    self.FIO_edit.setText(data[0])
                    self.command_combo.setCurrentText(data[1])
                    self.badge_number_edit.setText(data[2])
                    # Depending on your data format, you may need to handle gender separately
                    gender = data[3]
                    if gender == 'М':
                        self.male_rb.setChecked(True)
                    else:
                        self.female_rb.setChecked(True)
                    self.shooting_result_edit.setText(data[4])
                    self.running_result_edit.setText(data[5])
                    break

    def edit_player(self):
        selected_player_index = self.player_combo.currentIndex()

        with open("Players.txt", "r") as file:
            lines = file.readlines()

        new_data = f"{self.FIO_edit.text()}_{self.command_combo.currentText()}_{self.badge_number_edit.text()}_{'М' if self.male_rb.isChecked() else 'Ж'}_{self.shooting_result_edit.text()}_{self.running_result_edit.text()}\n"

        lines[selected_player_index] = new_data

        with open("Players.txt", "w") as file:
            file.writelines(lines)

        QtWidgets.QMessageBox.information(self, 'Успех', 'Игрок успешно изменен')


class DelPlayerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Удалить участника")
        self.setFixedSize(400, 100)

        self.setAttribute(Qt.WA_DeleteOnClose)

        layout = QtWidgets.QVBoxLayout()

        label = QLabel("Выберите участника, которого хотите удалить:")
        layout.addWidget(label)

        self.player_combo = QComboBox()
        self.load_players_from_file()
        layout.addWidget(self.player_combo)

        delete_button = QPushButton("Удалить участника")
        delete_button.clicked.connect(self.delete_player)
        layout.addWidget(delete_button)

        self.setLayout(layout)

    def load_players_from_file(self):
        with open("Players.txt", "r") as file:
            players = []
            for line in file:
                player_info = line.strip().split("_")
                if len(player_info) >= 4:
                    name_team_number = "_".join(player_info[:3])
                    players.append(name_team_number.replace("_", "    "))
            self.player_combo.addItems(players)

    def delete_player(self):
        selected_player_index = self.player_combo.currentIndex()

        with open("Players.txt", "r") as file:
            lines = file.readlines()

        del lines[selected_player_index]

        with open("Players.txt", "w") as file:
            file.writelines(lines)

        self.updateComboBox()  # Update combo box after deleting the player

        QMessageBox.information(self, 'Успех', 'Игрок успешно удален')

    def updateComboBox(self):
        with open("Players.txt", "r") as file:
            players = []
            for line in file:
                player_info = line.strip().split("_")
                if len(player_info) >= 4:
                    name_team_number = "_".join(player_info[:3])
                    players.append(name_team_number.replace("_", "    "))

        current_items = [self.player_combo.itemText(i) for i in range(self.player_combo.count())]

        if set(players) != set(current_items):
            self.player_combo.clear()
            self.player_combo.addItems(players)

class SuccessMessage(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Успех")
        self.setText("Итоговый протокол успешно сгенерирован")

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
        self.EditPlayer.setFont(font)
        self.EditPlayer.setObjectName("EditPlayer")
        self.DelPlayer = QtWidgets.QPushButton(self.centralwidget)
        self.DelPlayer.setGeometry(QtCore.QRect(40, 360, 311, 91))
        self.DelPlayer.setVisible(False)
        self.DelPlayer.setFont(font)
        self.DelPlayer.setObjectName("DelPlayer")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Back2 = QtWidgets.QPushButton(self.centralwidget)
        self.Back2.setGeometry(QtCore.QRect(40, 590, 211, 121))
        self.Back2.setVisible(False)
        self.Back2.setFont(font)
        self.Back2.setObjectName("Back2")
        self.Next2 = QtWidgets.QPushButton(self.centralwidget)
        self.Next2.setGeometry(QtCore.QRect(820, 600, 191, 111))
        self.Next2.setVisible(False)
        self.GenerateProtokol = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateProtokol.setGeometry(QtCore.QRect(630, 590, 400, 121))
        self.GenerateProtokol.setVisible(False)
        self.GenerateProtokol.setFont(font)
        self.GenerateProtokol.setObjectName("GenerateProtokol")
        self.Next2.setFont(font)
        self.Next2.setObjectName("Next")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(40, 590, 211, 121))
        self.Back.setFont(font)
        self.Back.setObjectName("Back")
        self.Back.setVisible(False)

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
        self.Duo.setGeometry(QtCore.QRect(50, 140, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Duo.setFont(font)
        self.Duo.setObjectName("Duo")
        self.Duo.setChecked(True)
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
        self.FIOSud = QtWidgets.QLineEdit(self.centralwidget)
        self.FIOSud.setGeometry(QtCore.QRect(530, 150, 511, 31))
        self.FIOSud.setObjectName("FIOSud")
        self.Sud = QtWidgets.QLabel(self.centralwidget)
        self.Sud.setGeometry(QtCore.QRect(530, 105, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Sud.setFont(font)
        self.Sud.setObjectName("Sud")
        self.FIOSec = QtWidgets.QLineEdit(self.centralwidget)
        self.FIOSec.setGeometry(QtCore.QRect(530, 270, 511, 31))
        self.FIOSec.setObjectName("FIOSec")
        self.Sec = QtWidgets.QLabel(self.centralwidget)
        self.Sec.setGeometry(QtCore.QRect(530, 230, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Sec.setFont(font)
        self.Sec.setObjectName("Sec")
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

        MainWindow.setAttribute(Qt.WA_DeleteOnClose)

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
        self.Duo.setText(_translate("MainWindow", "Двоеборье"))
        self.Swimming.setText(_translate("MainWindow", "Плавание"))
        self.RB.setText(_translate("MainWindow", "Рукопашный бой"))
        self.Next.setText(_translate("MainWindow", "Далее"))
        self.Next2.setText(_translate("MainWindow", "Далее"))
        self.AddPlayer.setText(_translate("MainWindow", "Добавить участника"))
        self.EditPlayer.setText(_translate("MainWindow", "Редактировать участника"))
        self.DelPlayer.setText(_translate("MainWindow", "Удалить участника"))
        self.Back2.setText(_translate("MainWindow", "Назад"))
        self.Sud.setText(_translate("MainWindow", "Введите ФИО главного судьи:"))
        self.Sec.setText(_translate("MainWindow", "Введите ФИО секретаря:"))
        self.GenerateProtokol.setText(_translate("MainWindow", "Сгенерировать"))

    def add_functions(self):
        self.FIOSec.textChanged.connect(self.checkFields)
        self.FIOSud.textChanged.connect(self.checkFields)
        self.Next.setEnabled(False)
        self.Next.clicked.connect(self.SecWind)
        self.Back.clicked.connect(self.FirstWind)
        self.Next2.clicked.connect(self.ThirdWind)
        self.Back2.clicked.connect(self.SecWind)
        self.AddTeam.clicked.connect(self.openAddTeamDialog)
        self.EditTeam.clicked.connect(self.openEditTeamDialog)
        self.DeleteTeam.clicked.connect(self.openDelTeamDialog)
        self.AddPlayer.clicked.connect(self.open_add_player_dialog)
        self.EditPlayer.clicked.connect(self.open_edit_player_dialog)
        self.DelPlayer.clicked.connect(self.open_del_player_dialog)
        self.GenerateProtokol.clicked.connect(lambda: CreateExel(self.FIOSud.text(), self.FIOSec.text()))
        self.GenerateProtokol.clicked.connect(self.show_success_message)

    def show_success_message(self):
        success_msg = SuccessMessage()
        success_msg.exec_()

    def checkFields(self):
        if self.FIOSec.text() and self.FIOSud.text():
            self.Next.setEnabled(True)
        else:
            self.Next.setEnabled(False)

    def ThirdWind(self):
        self.Changeurtype.setVisible(False)
        self.Duo.setVisible(False)
        self.Swimming.setVisible(False)
        self.RB.setVisible(False)
        self.Next.setVisible(False)
        self.Back.setVisible(False)
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
        self.Sec.setVisible(False)
        self.Sud.setVisible(False)
        self.FIOSec.setVisible(False)
        self.FIOSud.setVisible(False)
        self.GenerateProtokol.setVisible(True)
    def SecWind(self):
        self.Changeurtype.setVisible(False)
        self.Duo.setVisible(False)
        self.Swimming.setVisible(False)
        self.RB.setVisible(False)
        self.Next.setVisible(False)
        self.Back.setVisible(True)
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
        self.Sec.setVisible(False)
        self.Sud.setVisible(False)
        self.FIOSec.setVisible(False)
        self.FIOSud.setVisible(False)
        self.GenerateProtokol.setVisible(False)
    def FirstWind(self):
        self.Changeurtype.setVisible(True)
        self.Duo.setVisible(True)
        self.Swimming.setVisible(True)
        self.RB.setVisible(True)
        self.Next.setVisible(True)
        self.Back.setVisible(False)
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
        self.Sec.setVisible(True)
        self.Sud.setVisible(True)
        self.FIOSec.setVisible(True)
        self.FIOSud.setVisible(True)
        self.GenerateProtokol.setVisible(False)

    def openAddTeamDialog(self):
        dialog = AddTeamDialog()
        if dialog.exec_() == QDialog.Accepted:  # Проверяем, было ли добавлено значение
            team_name = dialog.textEdit.text()

    def openEditTeamDialog(self):
        dialog = EditTeamDialog()
        dialog.exec_()

    def openDelTeamDialog(self):
        dialog = DelTeamDialog()
        if dialog.exec_() == QDialog.Accepted:
            team_name = dialog.textEdit.text()

    def open_add_player_dialog(self):
        dialog = AddPlayerDialog()
        dialog.exec_()

    def open_edit_player_dialog(self):
        dialog = EditPlayerDialog()
        dialog.exec_()

    def open_del_player_dialog(self):
        dialog = DelPlayerDialog()
        dialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
