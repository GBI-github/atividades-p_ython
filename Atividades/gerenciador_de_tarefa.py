import tkinter as tk
from tkinter import messagebox


def adicionar_tarefa():
    taf = tarefa.get()
    if taf:
        lista_tarefa.insert(tk.END, taf)
        tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, insira uma tarefa.")


def remover_tarefa():
    try:
        selecionado = lista_tarefa.curselection()
        lista_tarefa.delete(selecionado)

    except:
        pass


def concluir_tarefa():
    try:
        selecionado = lista_tarefa.curselection()
        lista_tarefa.itemconfig(selecionado, {"bg": "light gray", "fg": "green"})

    except:
        pass


janela = tk.Tk()
janela.title("gerenciador")

tarefa = tk.Entry(janela, width=30)
tarefa.pack(pady=10)
tarefa.bind("<Return>", lambda event=None: adicionar_tarefa())

botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa)
botao_concluir = tk.Button(janela, text="Concluir Tarefa", command=concluir_tarefa)
botao_adicionar.pack()
botao_remover.pack()
botao_concluir.pack()

lista_tarefa = tk.Listbox(janela, selectbackground="white")
lista_tarefa.pack()

janela.mainloop()
