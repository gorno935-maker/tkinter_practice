import tkinter as tk

root = tk.Tk()
root.title("Информация")
root.geometry("400x220")

tk.Label(root, text="Информационная карточка",
         font=("Arial", 18, "bold")).pack(pady=(15, 10))
tk.Label(root, text="ФИО: Иванов Иван Иванович",
         font=("Arial", 12), fg="#1a4f8b").pack(pady=5)
tk.Label(root, text="Группа: ИС-21",
         font=("Arial", 12), fg="#1a4f8b").pack(pady=5)
tk.Label(root, text="Дисциплина: Программирование на Python",
         font=("Arial", 12), fg="#1a4f8b").pack(pady=5)

root.mainloop()