from PySide2 import QtWidgets
import sys
import os
import csv
from PySide2.QtWidgets import QMessageBox


class RegistrationWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Окно регистрации")
        self.setGeometry(300, 300, 300, 200)

        layout = QtWidgets.QGridLayout(self)

        label_login = QtWidgets.QLabel("Логин:")
        layout.addWidget(label_login, 0, 0)
        self.entry_login = QtWidgets.QLineEdit(self)
        layout.addWidget(self.entry_login, 0, 1)

        label_password = QtWidgets.QLabel("Пароль:")
        layout.addWidget(label_password, 1, 0)
        self.entry_password = QtWidgets.QLineEdit(self)
        self.entry_password.setEchoMode(QtWidgets.QLineEdit.Password)
        layout.addWidget(self.entry_password, 1, 1)

        label_confirm_password = QtWidgets.QLabel("Подтвердите пароль:")
        layout.addWidget(label_confirm_password, 2, 0)
        self.entry_confirm_password = QtWidgets.QLineEdit(self)
        self.entry_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        layout.addWidget(self.entry_confirm_password, 2, 1)

        label_role = QtWidgets.QLabel("Роль:")
        layout.addWidget(label_role, 3, 0)
        self.combo_role = QtWidgets.QComboBox(self)
        self.combo_role.addItems(["Ученик", "Учитель"])
        layout.addWidget(self.combo_role, 3, 1)

        btn_register = QtWidgets.QPushButton("Зарегистрироваться", self)
        btn_register.clicked.connect(self.register)
        layout.addWidget(btn_register, 4, 0, 1, 2)

        self.setLayout(layout)

    def register(self):
        login_ = self.entry_login.text()
        password = self.entry_password.text()
        confirm_password = self.entry_confirm_password.text()
        role = self.combo_role.currentText()

        if password == confirm_password:
            file_path = r'C:\Users\user\Desktop\project programm\users.csv'

            if not self.is_login_unique(login_, file_path):
                QMessageBox.warning(self, "Ошибка", "Пользователь с таким логином уже существует.")
                return

            with open(file_path, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([login_, password, role])

            QMessageBox.information(self, "Успешно", "Регистрация прошла успешно!")
        else:
            QMessageBox.warning(self, "Ошибка", "Пароли не совпадают!")

    def is_login_unique(self, login_, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row[0] == login_:
                        return False
        return True
