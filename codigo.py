import tkinter as tk
from tkinter import scrolledtext

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry("280x400")  
        self.config(bg="#222222")

        self.history = []  

        self.create_widgets()

    def create_widgets(self):
        entry_frame = tk.Frame(self, bg="#222222")
        entry_frame.pack(fill="x")

        self.entry = tk.Entry(entry_frame, font=("Arial", 20), fg="white", bg="#444444", bd=2, relief="flat", justify="right")
        self.entry.pack(fill="x", padx=10, pady=10)

        buttons_frame = tk.Frame(self, bg="#222222")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)  

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("/", 4, 3),
            ("(", 5, 0), (")", 5, 1), ("CE", 5, 2), ("^", 5, 3),
            ("sqrt", 6, 0), ("sin", 6, 1), ("cos", 6, 2), ("tan", 6, 3),
            ("log", 7, 0), ("exp", 7, 1), ("pi", 7, 2), ("^2", 7, 3),
            ("%", 8, 0), (",", 8, 1) 
        ]

        for (text, row, col) in buttons:
            button = tk.Button(buttons_frame, text=text, font=("Arial", 14), fg="white", bg="#333333", bd=2, relief="flat", command=lambda t=text: self.click_button(t))
            button.grid(row=row, column=col, padx=3, pady=3, sticky="nsew") 
        # Adicionando o botão para exibir o histórico
        history_button = tk.Button(self, text="Histórico", font=("Arial", 12), fg="white", bg="#444444", bd=2, relief="flat", command=self.show_history)
        history_button.pack(side="bottom", fill="x", padx=10, pady=5)

        # Definindo pesos das linhas e colunas para que os botões se expandam uniformemente
        for i in range(8):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def click_button(self, button):
        if button == "CE":
            self.entry.delete(0, tk.END)
        elif button == "=":
            try:
                if self.entry.get():
                    expr = self.entry.get()
                    # Usar o eval para calcular a expressão
                    result = eval(expr)
                    self.history.append(expr + " = " + str(result))  # Adicionar a expressão e o resultado ao histórico
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Erro")
        elif button == "C":
            self.clear_entry()
        elif button == "%":
            expression = self.entry.get()
            try:
                # Avaliar a expressão existente para obter o valor
                value = eval(expression)
                # Calcular a porcentagem
                result = value / 100
                # Se o resultado for um número inteiro, forçar a exibição com duas casas decimais
                if result == int(result):
                    result_formatted = "{:.2f}".format(result)
                else:
                    result_formatted = str(result)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result_formatted)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Erro")
        else:
            self.entry.insert(tk.END, button)

    def show_history(self):
        # Criar uma janela pop-up para exibir o histórico
        history_window = tk.Toplevel(self)
        history_window.title("Histórico")
        history_window.geometry("400x300")
        history_window.config(bg="#222222")

        # Adicionando uma área de texto com barra de rolagem
        history_text = scrolledtext.ScrolledText(history_window, font=("Arial", 12), fg="white", bg="#444444", bd=2, relief="flat")
        history_text.pack(expand=True, fill="both", padx=10, pady=10)

        # Preencher o texto da janela com os cálculos no histórico
        for item in self.history:
           history_text.insert(tk.END, item + "\n")
           history_text.tag_add("white", "1.0", "end")
           history_text.tag_config("black", foreground="black")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
