print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 033\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DUPLA LISTA' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
lista_principal = []
sublista_temporario = []
print(f"\033[32m{'ORGANIZADOR DE PRODUTO' :^32}\033[0m")

while True:
    escolha = str(input("Deseja adicionar algum item? [S/N]: ")).strip().lower()[0]
    if escolha == "s":
        while True:
            sublista_temporario.append(str(input("Nome: ")))
            sublista_temporario.append(float(input("Preço: ")))
            sublista_temporario.append(int(input("Estoque: ")))
            lista_principal.append(sublista_temporario[:])
            sublista_temporario.clear()
            esc1 = str(input("Deseja Continuar? [S/N]: ")).strip().lower()
            if esc1 != "s":
                break
    break


import tkinter as tk
from tkinter import ttk


janela = tk.Tk()
janela.title("Tabela de preço")


tabela = ttk.Treeview(janela, columns=("Nome  ", "Preço  ", "Estoque  "))
tabela.heading("#1", text="Nome     ")
tabela.heading("#2", text="Preço    ")
tabela.heading("#3", text="Estoque  ")

for coluna in ("#1", "#2", "#3"):
    tabela.column(coluna, anchor="center")

for dado in lista_principal:
    tabela.insert("", "end", values=dado)


tabela.pack()

janela.mainloop()
