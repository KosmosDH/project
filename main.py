from PySide2 import QtWidgets
import sys
import os
import csv
from PySide2.QtWidgets import QMessageBox
import registration_window, login_window

class MainApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Главное меню")
        self.setGeometry(300, 300, 600, 400)

        self.stack = QtWidgets.QStackedWidget(self)
        self.loginWindow = LoginWindow()
        self.registrationWindow = RegistrationWindow()

        self.stack.addWidget(self.loginWindow)
        self.stack.addWidget(self.registrationWindow)

        self.loginButton = QtWidgets.QPushButton("Войти", self)
        self.loginButton.clicked.connect(self.displayLogin)
        self.loginButton.setGeometry(10, 350, 100, 40)

        self.registerButton = QtWidgets.QPushButton("Зарегистрироваться", self)
        self.registerButton.clicked.connect(self.displayRegistration)
        self.registerButton.setGeometry(120, 350, 150, 40)

    def displayLogin(self):
        self.stack.setCurrentWidget(self.loginWindow)

    def displayRegistration(self):
        self.stack.setCurrentWidget(self.registrationWindow)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec_())
