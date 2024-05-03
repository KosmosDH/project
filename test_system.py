from PySide2 import QtWidgets, QtCore
import random
import json

question_number = 0
correct_answers = 0


class TestSystem(QtWidgets.QWidget):
    def __init__(self, filename):
        super().__init__()
        self.setWindowTitle("Тестирующая система")
        self.setGeometry(100, 100, 600, 400)
        self.questions = self.open_file(filename)
        self.initUI()

    def open_file(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            questions = json.load(file)
            random.shuffle(questions)
            questions = questions[:10]
        return questions

    def initUI(self):
        self.layout = QtWidgets.QVBoxLayout(self)

        self.title_label = QtWidgets.QLabel("Тестирующая система", self)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.start_button = QtWidgets.QPushButton("Начать тест", self)
        self.start_button.clicked.connect(self.start_test)
        self.layout.addWidget(self.start_button)

        self.quit_button = QtWidgets.QPushButton("Выйти", self)
        self.quit_button.clicked.connect(self.close)
        self.layout.addWidget(self.quit_button)

    def start_test(self):
        self.show_question()

    def show_question(self):
        global question_number, correct_answers

        for widget in self.findChildren(QtWidgets.QWidget):
            widget.deleteLater()

        if question_number < len(self.questions):
            current_question = self.questions[question_number]
            question_text = current_question["question"]
            question_type = current_question["type"]
            correct_answer = current_question["answer"]
            answer_options = current_question["options"]

            self.question_label = QtWidgets.QLabel(question_text, self)
            self.layout.addWidget(self.question_label)

            self.number_label = QtWidgets.QLabel(f"Вопрос {question_number + 1} из {len(self.questions)}", self)
            self.layout.addWidget(self.number_label)

            if question_type == "выбор":
                self.var = QtWidgets.QButtonGroup(self)
                for option in answer_options:
                    radio = QtWidgets.QRadioButton(option, self)
                    self.var.addButton(radio)
                    self.layout.addWidget(radio)
            elif question_type == "писать":
                self.entry = QtWidgets.QLineEdit(self)
                self.layout.addWidget(self.entry)

            self.button = QtWidgets.QPushButton("Ответить", self)
            self.button.clicked.connect(lambda: self.check_answer(correct_answer, question_type))
            self.layout.addWidget(self.button)

        else:
            self.result_label = QtWidgets.QLabel(
                f"Вы ответили правильно на {correct_answers} из {len(self.questions)} вопросов.", self)
            self.layout.addWidget(self.result_label)

            self.quit_button = QtWidgets.QPushButton("Выйти", self)
            self.quit_button.clicked.connect(self.close)
            self.layout.addWidget(self.quit_button)

    def check_answer(self, correct_answer, question_type):
        global question_number, correct_answers
        user_answer = ""
        if question_type == "выбор":
            user_answer = self.var.checkedButton().text()
        elif question_type == "писать":
            user_answer = self.entry.text()

        if user_answer.lower() == correct_answer.rstrip().lower():
            correct_answers += 1
            QtWidgets.QMessageBox.information(self, "Правильно!", "Вы ответили правильно!")
        else:
            QtWidgets.QMessageBox.warning(self, "Неправильно!",
                                          f"Вы ответили неправильно. Правильный ответ: {correct_answer}")

        question_number += 1
        self.show_question()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    test_system = TestSystem(r"C:\Users\user\Desktop\project programm/tests/test_20240503104347.json")
    test_system.show()
    app.exec_()
