import tkinter as tk
from tkinter import messagebox
import json


class LoginTab:
    def __init__(self):
        with open(r'C:\Users\user\Desktop\project programm\login.txt', "r", encoding="utf-8") as file:
            self.existing_data = [line.strip().split("|") for line in file.readlines()]

    def login(self):
        login_ = self.entry_login.get()
        password = self.entry_password.get()
        flag = 0
        for data in self.existing_data:
            if data[0] == login_ and data[1] == password:
                flag = 1
                messagebox.showinfo("Успешно", "Вы вошли в аккаунт!")
                if data[2] == "Ученик":
                    self.window.destroy()
                    import student_menu
                elif data[2] == "Учитель":
                    self.window.destroy()
                    import test
                break
        if not flag:
            messagebox.showinfo("Неудача", "Не правильно введен логин или пароль!")

    def create_widgets(self):
        self.window = tk.Tk()
        self.window.title("Вход в аккаунт")
        self.window.geometry("600x400")

        label_login = tk.Label(self.window, text="Логин:")
        label_login.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry_login = tk.Entry(self.window)
        self.entry_login.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)

        label_password = tk.Label(self.window, text="Пароль:")
        label_password.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.entry_password = tk.Entry(self.window)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)

        btn = tk.Button(self.window, text="Войти", command=self.login)
        btn.grid(row=4, columnspan=2, padx=10, pady=5, sticky=tk.W)

    # def get_login(self):
    #    return self.entry_login.get()

    def run(self):
        self.create_widgets()
        self.window.mainloop()

# window.mainloop()
