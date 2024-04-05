import tkinter as tk
import json
import os
from datetime import datetime


class TestCreator:
    def __init__(self):
        self.tests_directory = r"C:\Users\user\Desktop\project programm\tests"
        if not os.path.exists(self.tests_directory):
            os.makedirs(self.tests_directory)

        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.filename = f"test_{self.timestamp}.json"

        self.window = tk.Tk()
        self.window.title("Меню учителя")
        self.var = tk.StringVar()
        self.setup_ui()

    def save_question(self):
        question = self.entry_question.get()
        choice = self.var.get()
        answer = self.entry_answer.get()
        options = self.entry_options.get().split(',')
        question_data = {
            "question": question,
            "type": choice,
            "answer": answer,
            "options": options
        }

        file_path = os.path.join(self.tests_directory, self.filename)

        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump([question_data], file, ensure_ascii=False, indent=4)
        else:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            data.append(question_data)

            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Вопрос сохранен в файле {self.filename}")

    def setup_ui(self):
        # Labels
        label_question = tk.Label(self.window, text="Вопрос:")
        label_choice = tk.Label(self.window, text="Ответ выборочный или письменный?")
        label_answer = tk.Label(self.window, text="Ответ на вопрс:")
        label_options = tk.Label(self.window, text="Варианты ответов, если есть:")

        # Entry
        self.entry_question = tk.Entry(self.window)
        choice1 = tk.Radiobutton(self.window, text="письменно", value="писать", variable=self.var, font=("Arial", 12))
        choice2 = tk.Radiobutton(self.window, text="выбор", value="выбор", variable=self.var, font=("Arial", 12))
        self.entry_answer = tk.Entry(self.window)
        self.entry_options = tk.Entry(self.window)

        # Save btn
        btn = tk.Button(self.window, text="Сохранить", command=self.save_question)

        # Layout
        label_question.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        label_choice.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        label_answer.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        label_options.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry_question.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_answer.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_options.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        choice2.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        choice1.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        btn.grid(row=4, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.window.mainloop()


