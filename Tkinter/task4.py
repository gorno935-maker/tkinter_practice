import tkinter as tk


def show_data():
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    if not name or not age:
        result.config(text="Пожалуйста, заполните все поля")
    else:
        result.config(text=f"{name}, вам {age} лет")


root = tk.Tk()
root.title("Форма ввода данных")
root.geometry("350x200")

tk.Label(root, text="Имя:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_name = tk.Entry(root, width=25)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Возраст:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_age = tk.Entry(root, width=25)
entry_age.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Показать данные", command=show_data).grid(
    row=2, column=0, columnspan=2, pady=10)

result = tk.Label(root, text="", font=("Arial", 12))
result.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()