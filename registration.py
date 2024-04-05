import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as messagebox


def save_data():
    login = entry_login.get()
    password = entry_password.get()
    role = role_var.get()

    existing_logins = [data[0] for data in existing_data]

    if login in existing_logins:
        messagebox.showerror("Ошибка", "Такой пользователь уже существует.")
    else:
        data = f"{login}|{password}|{role}\n"
        with open(r'C:\Users\user\Desktop\project programm\login.txt', "a", encoding="utf-8") as file:
            file.write(data)
        messagebox.showinfo("Успешно", "Данные сохранены успешно.")
        window.destroy()
        import main


with open(r'C:\Users\user\Desktop\project programm\login.txt', "r", encoding="utf-8") as file:
    existing_data = [line.strip().split("|") for line in file.readlines()]

window = tk.Tk()
window.title("Регистрационная форма")
window.geometry("600x400")

label_login = tk.Label(window, text="Логин:")
label_login.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
entry_login = tk.Entry(window)
entry_login.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)

label_password = tk.Label(window, text="Пароль:")
label_password.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
entry_password = tk.Entry(window)
entry_password.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)

label_role = tk.Label(window, text="Роль:")
label_role.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
roles = ["Учитель", "Ученик"]
role_var = tk.StringVar(window)
role_var.set(roles[0])
role_dropdown = tk.OptionMenu(window, role_var, *roles)
role_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

btn = tk.Button(window, text="Зарегистрироваться", command=save_data)
btn.grid(row=4, columnspan=2, padx=10, pady=5, sticky=tk.W)

window.mainloop()
