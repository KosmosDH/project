from PySide2 import QtWidgets
import sys
import os
import csv
from PySide2.QtWidgets import QMessageBox


class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Окно входа")
        self.setGeometry(300, 300, 300, 200)

        layout = QtWidgets.QGridLayout(self)

        # Логин
        label_login = QtWidgets.QLabel("Логин:")
        layout.addWidget(label_login, 0, 0)
        self.entry_login = QtWidgets.QLineEdit(self)
        layout.addWidget(self.entry_login, 0, 1)

        label_password = QtWidgets.QLabel("Пароль:")
        layout.addWidget(label_password, 1, 0)
        self.entry_password = QtWidgets.QLineEdit(self)
        self.entry_password.setEchoMode(QtWidgets.QLineEdit.Password)
        layout.addWidget(self.entry_password, 1, 1)

        btn_login = QtWidgets.QPushButton("Войти", self)
        btn_login.clicked.connect(self.login)
        layout.addWidget(btn_login, 2, 0, 1, 2)

        self.setLayout(layout)

    def login(self):
        login_ = self.entry_login.text()
        password = self.entry_password.text()
        flag = False

        file_path = r'C:\Users\user\Desktop\project programm\users.csv'

        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == login_ and row[1] == password:
                    flag = True
                    QMessageBox.information(self, "Успешно", "Вы вошли в аккаунт!")
                    role = row[2]
                    if role == "Ученик":
                        # код для открытия окна теста
                        pass
                    elif role == "Учитель":
                        # код для открытия окна создания теста
                        pass
                    break

        if not flag:
            QMessageBox.information(self, "Неудача", "Не правильно введен логин или пароль!")
