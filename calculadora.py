import tkinter as tk
from math import sqrt, pow

# Função para inserir texto no visor
def inserir(valor):
    entrada_var.set(entrada_var.get() + str(valor))

# Função para limpar o visor
def limpar():
    entrada_var.set("")

# Função para calcular o resultado
def calcular():
    try:
        expressao = entrada_var.get()
        resultado = eval(expressao, {"__builtins__": None}, {"sqrt": sqrt, "pow": pow})
        entrada_var.set(str(resultado))
    except Exception as e:
        entrada_var.set("Erro")

# Função para apagar o último caractere
def apagar():
    entrada_var.set(entrada_var.get()[:-1])

# Janela principal
janela = tk.Tk()
janela.title("Calculadora")

entrada_var = tk.StringVar()

# Campo de entrada
entrada = tk.Entry(janela, textvariable=entrada_var, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Lista de botões (linhas de botões)
botoes = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '(', '+'],
    [')',  'C','<-','='],
]

# Criar os botões dinamicamente
for i, linha in enumerate(botoes):
    for j, botao in enumerate(linha):
        if botao == '':
            continue
        elif botao == '=':
            tk.Button(janela, text=botao, width=5, height=2, font=("Ivy", 14),
                      command=calcular).grid(row=i+1, column=j, sticky="nsew")
        elif botao == 'C':
            tk.Button(janela, text=botao, width=5, height=2, font=("Ivy", 14),
                      command=limpar).grid(row=i+1, column=j, sticky="nsew")
        elif botao == '<-':
            tk.Button(janela, text=botao, width=5, height=2, font=("Ivy", 14),
                      command=apagar).grid(row=i+1, column=j, sticky="nsew")
        else:
            tk.Button(janela, text=botao, width=5, height=2, font=("Ivy", 14),
                      command=lambda b=botao: inserir(b)).grid(row=i+1, column=j, sticky="nsew")

# Tornar os botões responsivos
for i in range(7):
    janela.rowconfigure(i, weight=1)
for j in range(4):
    janela.columnconfigure(j, weight=1)

# Iniciar interface
janela.mainloop()
