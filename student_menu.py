import tkinter as tk
from tkinter import filedialog
import os
from test_system import start

window = tk.Tk()
window.title("Вход в аккаунт")
window.geometry("600x400")

selected_item_text = ""


def import_files():
    file_paths = filedialog.askopenfilenames(title="Выберите файлы", filetypes=[("Text files", "*.json")])

    if file_paths:
        for file_path in file_paths:
            file_listbox.insert(tk.END, os.path.basename(file_path))
        status_label.config(text=f"Выбрано файлов: {len(file_paths)}")


def run_selected_file(self):
    global selected_item_text
    selected_index = file_listbox.curselection()
    if selected_index:
        selected_item_text = file_listbox.get(selected_index[0])
        window.destroy()
    start(selected_index)


def read_login_file():
    with open('login', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('|')
            if parts[2] == 'Ученик':
                return parts[0]


username = tk.Label()

file_listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)
file_listbox.pack(pady=10)
file_listbox.bind("<Double-Button-1>", run_selected_file)

import_button = tk.Button(window, text="Импортировать файлы", command=import_files)
import_button.pack(pady=10)


status_label = tk.Label(window, text="")
status_label.pack()

login_label = tk.Label(window, text=read_login_file())
login_label.pack(anchor='nw')

window.mainloop()
