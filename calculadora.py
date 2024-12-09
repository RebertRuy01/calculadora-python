import tkinter as tk
from tkinter import messagebox
import math

# Função para adicionar números ao visor
def adicionar_ao_visor(num):
    entrada.set(entrada.get() + str(num))

# Função para limpar o visor
def limpar_visor():
    entrada.set("")

# Função para calcular o resultado da expressão
def calcular():
    try:
        resultado = eval(entrada.get())  # Avalia a expressão no visor
        entrada.set(resultado)
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero não é permitida!")
        entrada.set("")
    except Exception:
        messagebox.showerror("Erro", "Expressão inválida!")
        entrada.set("")

# Função para calcular a raiz quadrada
def raiz_quadrada():
    try:
        valor = float(entrada.get())
        entrada.set(math.sqrt(valor))
    except Exception:
        messagebox.showerror("Erro", "Entrada inválida para raiz quadrada!")
        entrada.set("")

# Função para calcular potência (x^y)
def potencia():
    entrada.set(entrada.get() + "**")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.resizable(False, False)

# Variável para o visor
entrada = tk.StringVar()

# Campo de entrada (visor)
visor = tk.Entry(janela, textvariable=entrada, font=("Arial", 18), justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões da calculadora
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
    ('√', 5, 0), ('^', 5, 1), ('=', 5, 2)
]

# Criação e posicionamento dos botões
for (texto, linha, coluna) in botoes:
    if texto == "=":
        botao = tk.Button(janela, text=texto, width=5, height=2, bg="green", fg="white",
                          font=("Arial", 14), command=calcular)
    elif texto == "C":
        botao = tk.Button(janela, text=texto, width=5, height=2, bg="red", fg="white",
                          font=("Arial", 14), command=limpar_visor)
    elif texto == "√":
        botao = tk.Button(janela, text=texto, width=5, height=2, bg="blue", fg="white",
                          font=("Arial", 14), command=raiz_quadrada)
    elif texto == "^":
        botao = tk.Button(janela, text=texto, width=5, height=2, bg="purple", fg="white",
                          font=("Arial", 14), command=potencia)
    else:
        botao = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 14),
                          command=lambda t=texto: adicionar_ao_visor(t))
    botao.grid(row=linha, column=coluna, padx=5, pady=5)

# Iniciar o loop da interface
janela.mainloop()