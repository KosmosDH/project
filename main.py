import tkinter as tk
import login


window = tk.Tk()
window.title("Главное меню")
window.geometry("600x400")
login_var = login.LoginTab()


def logining():
    window.destroy()
    login_var.run()


def registration():
    window.destroy()
    import registration


button = tk.Button(window, text="Войти", command=logining)
button.grid(row=100, columnspan=2, padx=10, pady=5, sticky=tk.W)

button = tk.Button(window, text="Зарегистрироваться", command=registration)
button.grid(row=4, columnspan=2, padx=10, pady=5, sticky=tk.W)

window.mainloop()
