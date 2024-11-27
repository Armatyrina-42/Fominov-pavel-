import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Division by zero!"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Invalid input")


def checkbox_clicked():
    choices = []
    if var1.get():
        choices.append("Первый")
    if var2.get():
        choices.append("Второй")
    if var3.get():
        choices.append("Третий")

    if choices:
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(choices)}")
    else:
        messagebox.showwarning("Выбор", "Вы ничего не выбрали")


def open_file():
    filepath = filedialog.askopenfilename(
        defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if filepath:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                text = file.read()
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, text)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при открытии файла: {e}")


root = tk.Tk()
root.title("Фоминов П.А.")

# Notebook (tabs)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Calculator
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Калькулятор")

entry_num1 = tk.Entry(tab1)
entry_num1.grid(row=0, column=0)

operation_var = tk.StringVar(tab1)
operation_var.set("+")
operation_menu = tk.OptionMenu(tab1, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=0, column=1)

entry_num2 = tk.Entry(tab1)
entry_num2.grid(row=0, column=2)

calculate_button = tk.Button(tab1, text="Вычислить", command=calculate)
calculate_button.grid(row=0, column=3)

result_label = tk.Label(tab1, text="Результат:")
result_label.grid(row=1, column=0, columnspan=4)

# Checkboxes
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Чекбоксы")

var1 = tk.BooleanVar()
check1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
check1.pack()

var2 = tk.BooleanVar()
check2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
check2.pack()

var3 = tk.BooleanVar()
check3 = tk.Checkbutton(tab2, text="Третий", variable=var3)
check3.pack()

checkbox_button = tk.Button(tab2, text="Показать выбор", command=checkbox_clicked)
checkbox_button.pack()

# Text Editor
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Текстовый редактор")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Открыть", command=open_file)
menubar.add_cascade(label="Файл", menu=filemenu)
root.config(menu=menubar)

text_area = tk.Text(tab3, wrap=tk.WORD)
text_area.pack(expand=True, fill="both")

root.mainloop()
