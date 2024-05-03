import tkinter as tk
import tkinter.filedialog as fd
import json
import os
from datetime import datetime

tests_directory = r"C:\Users\user\Desktop\project programm\tests"
if not os.path.exists(tests_directory):
    os.makedirs(tests_directory)

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
filename = f"test_{timestamp}.json"

window = tk.Tk()
window.title("Меню учителя")
var = tk.StringVar()


def save_question():
    question = entry_question.get()
    choice = var.get()
    answer = entry_answer.get()
    options = entry_options.get().split(',')
    question_data = {
        "question": question,
        "type": choice,
        "answer": answer,
        "options": options
    }

    file_path = os.path.join(tests_directory, filename)

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([question_data], file, ensure_ascii=False, indent=4)
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        data.append(question_data)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Вопрос сохранен в файле {filename}")


# Labels
label_question = tk.Label(window, text="Вопрос:")
label_choice = tk.Label(window, text="Ответ выборочный или письменный?")
label_answer = tk.Label(window, text="Ответ на вопрс:")
label_options = tk.Label(window, text="Варианты ответов, если есть:")

# Entry
entry_question = tk.Entry(window)
choice1 = tk.Radiobutton(window, text="письменно", value="писать", variable=var, font=("Arial", 12))
choice2 = tk.Radiobutton(window, text="выбор", value="выбор", variable=var, font=("Arial", 12))
entry_answer = tk.Entry(window)
entry_options = tk.Entry(window)

# Save btn
btn = tk.Button(window, text="Сохранить", command=save_question)

# Layout
label_question.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
label_choice.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
label_answer.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
label_options.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
entry_question.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
entry_answer.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
entry_options.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
choice2.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
choice1.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
btn.grid(row=4, columnspan=2, padx=10, pady=5, sticky=tk.W)

window.mainloop()
