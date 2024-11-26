import tkinter as tk
from tkinter import messagebox, filedialog

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ФИО автора")
        self.geometry("400x300")

        # Создаем вкладки
        self.tab_control = tk.Notebook(self)
        self.tab1 = tk.Frame(self.tab_control)
        self.tab2 = tk.Frame(self.tab_control)
        self.tab3 = tk.Frame(self.tab_control)

        self.tab_control.add(self.tab1, text='Калькулятор')
        self.tab_control.add(self.tab2, text='Чекбоксы')
        self.tab_control.add(self.tab3, text='Работа с текстом')

        self.tab_control.pack(expand=1, fill='both')

        # Вкладка 1: Калькулятор
        self.create_calculator_tab()

        # Вкладка 2: Чекбоксы
        self.create_checkbox_tab()

        # Вкладка 3: Работа с текстом
        self.create_text_tab()

    def create_calculator_tab(self):
        self.num1_label = tk.Label(self.tab1, text="Число 1:")
        self.num1_label.pack()
        self.num1_entry = tk.Entry(self.tab1)
        self.num1_entry.pack()

        self.num2_label = tk.Label(self.tab1, text="Число 2:")
        self.num2_label.pack()
        self.num2_entry = tk.Entry(self.tab1)
        self.num2_entry.pack()

        self.operation_label = tk.Label(self.tab1, text="Операция:")
        self.operation_label.pack()
        self.operation_var = tk.StringVar(self.tab1)
        self.operation_var.set("+")
        self.operation_menu = tk.OptionMenu(self.tab1, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.pack()

        self.calculate_button = tk.Button(self.tab1, text="Вычислить", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(self.tab1, text="Результат:")
        self.result_label.pack()
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(self.tab1, textvariable=self.result_var, state='readonly')
        self.result_entry.pack()

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Ошибка", "Деление на ноль невозможно")
                    return

            self.result_var.set(result)
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа")

    def create_checkbox_tab(self):
        self.checkbox_vars = [tk.BooleanVar() for _ in range(3)]
        self.checkboxes = []

        for i, var in enumerate(self.checkbox_vars):
            checkbox = tk.Checkbutton(self.tab2, text=f"Вариант {i+1}", variable=var)
            checkbox.pack()
            self.checkboxes.append(checkbox)

        self.show_selection_button = tk.Button(self.tab2, text="Показать выбор", command=self.show_selection)
        self.show_selection_button.pack()

    def show_selection(self):
        selected = [i+1 for i, var in enumerate(self.checkbox_vars) if var.get()]
        if selected:
            messagebox.showinfo("Выбор", f"Вы выбрали варианты: {', '.join(map(str, selected))}")
        else:
            messagebox.showinfo("Выбор", "Вы ничего не выбрали")

    def create_text_tab(self):
        self.text_area = tk.Text(self.tab3, height=10, width=50)
        self.text_area.pack()

        self.load_button = tk.Button(self.tab3, text="Загрузить текст", command=self.load_text)
        self.load_button.pack()

    def load_text(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, text)

if __name__ == "__main__":
    app = App()
    app.mainloop()
