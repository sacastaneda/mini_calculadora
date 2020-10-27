import tkinter as tk
from tkinter import ttk
def init_window():
    window = tk.Tk()
    window.title("ejercicio")
    window.geometry('400x250')

    label = tk.Label(window, text='Calculadora', font=('Arial bold', 15))
    label.grid(column=0, row=0)

    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)

    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    label_entrada1 = tk.Label(window, text='Ingrese el primer numero', font=('Arial bold', 10))
    label_entrada1.grid(column=0, row=1)

    label_entrada2 = tk.Label(window, text='Ingrese el segundo numero', font=('Arial bold', 10))
    label_entrada2.grid(column=0, row=2)

    label_operator = tk.Label(window, text='Elija un operador', font=('Arial bold', 10))
    label_operator.grid(column=0, row=3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+', '-', '*', '/', 'pow']
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    label_resultado = tk.Label(window, text='Resultado:', font=('Arial bodl', 14))
    label_resultado.grid(column=0, row=6)

    boton_resultado = tk.Button(window, command= lambda: click_calcular(
                                                label_resultado,
                                                entrada1.get(),
                                                entrada2.get(),
                                                combo_operadores.get()),
                                        text='Calcular',
                                        bg='green',
                                        fg='white')
    boton_resultado.grid(column=1, row=5)
    window.mainloop()
def calculadora(num1, num2, ope):
    if ope == "+":
        resultado = int(num1) + int(num2)
    elif ope == "-":
        resultado = int(num1) - int(num2)
    elif ope == "*":
        resultado = int(num1) * int(num2)
    elif ope == "/":
        resultado = round((int(num1) / int(num2)), 2)
    elif ope == "pow":
        resultado = int(num1) ** int(num2)
    return resultado
def click_calcular(label, num1, num2, ope):
    valor1 = float(num1)
    valor2 = float(num2)
    res = calculadora(num1, num2, ope)
    label.configure(text='Resultado:'+str(res))
def main():
    init_window()
main()
