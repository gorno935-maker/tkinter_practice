import tkinter as tk


def change_text():
    label.config(text="Задание выполнено!")


root = tk.Tk()
root.title("Кнопка и обработчик")
root.geometry("350x150")

label = tk.Label(root, text="Нажмите кнопку", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Выполнить", command=change_text)
button.pack(pady=5)

root.mainloop()