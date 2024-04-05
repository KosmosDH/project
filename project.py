import random
import tkinter as tk
from tkinter import messagebox
import json


class TestingSystem:
    def __init__(self, filename):
        self.window = tk.Tk()
        self.window.title("Тестирующая система")
        self.window.geometry("600x400")
        self.filename = filename
        self.questions = self.open_file()
        self.question_number = 0
        self.correct_answers = 0
        self.create_widgets()

    def open_file(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            questions = json.load(file)
            random.shuffle(questions)
            return questions[:10]

    def show_question(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        if self.question_number < len(self.questions):
            current_question = self.questions[self.question_number]
            question_text = current_question["question"]
            question_type = current_question["type"]
            correct_answer = current_question["answer"]
            answer_options = current_question["options"]
            question_label = tk.Label(self.window, text=question_text, font=("Arial", 16))
            question_label.pack(pady=20)
            number_label = tk.Label(self.window, text=f"Вопрос {self.question_number + 1} из {len(self.questions)}")
            number_label.pack()

            if question_type == "выбор":
                self.var = tk.StringVar()
                for option in answer_options:
                    radio = tk.Radiobutton(self.window, text=option, value=option, variable=self.var, font=("Arial", 12))
                    radio.pack(anchor="w")
                button = tk.Button(self.window, text="Ответить", command=lambda: self.check_answer(correct_answer, question_type), font=("Arial", 12))
                button.pack(pady=10)
            elif question_type == "писать":
                self.entry = tk.Entry(self.window, font=("Arial", 12))
                self.entry.pack()
                button = tk.Button(self.window, text="Ответить", command=lambda: self.check_answer(correct_answer, question_type), font=("Arial", 12))
                button.pack(pady=10)
        else:
            result_label = tk.Label(self.window,
                                    text=f"Вы ответили правильно на {self.correct_answers} из {len(self.questions)} вопросов.",
                                    font=("Arial", 16))
            result_label.pack(pady=20)
            quit_button = tk.Button(self.window, text="Выйти", command=self.window.quit, font=("Arial", 12))
            quit_button.pack(pady=10)

    def check_answer(self, correct_answer, question_type):
        user_answer = ""
        if question_type == "выбор":
            user_answer = self.var.get()
        elif question_type == "писать":
            user_answer = self.entry.get()

        if user_answer.lower() == correct_answer.rstrip().lower():
            self.correct_answers += 1
            messagebox.showinfo("Правильно!", "Вы ответили правильно!")
        else:
            messagebox.showerror("Неправильно!", f"Вы ответили неправильно. Правильный ответ: {correct_answer}")
        self.question_number += 1
        self.show_question()

    def create_widgets(self):
        title_label = tk.Label(self.window, text="Тестирующая система", font=("Arial", 20))
        title_label.pack(pady=20)
        start_button = tk.Button(self.window, text="Начать тест", command=self.show_question, font=("Arial", 12))
        start_button.pack(pady=10)
        quit_button = tk.Button(self.window, text="Выйти", command=self.window.quit, font=("Arial", 12))
        quit_button.pack(pady=10)

    def run(self):
        self.window.mainloop()

# window.mainloop()
