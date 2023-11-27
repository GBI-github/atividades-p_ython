import time
from random import randint
from time import sleep
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 91 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DICIONARIO' :^32}\033[0m")
print()
print(f"\033[32m{'DADO':^32}\033[0m")
print()
ordem_dados = dict()
lista = []
lista1 = []

ordem_dados['jogador1'] = randint(1, 6)
ordem_dados['jogador2'] = randint(1, 6)
ordem_dados['jogador3'] = randint(1, 6)
ordem_dados['jogador4'] = randint(1, 6)

for k, v in ordem_dados.items():
    print(f"{k} rodou {v}")
    sleep(1)

for c in range(0, 5):
    c = f"jogador{c}"
    lista.append(c)
    lista1.append(lista[:])
    lista.clear()

for c in range(1, 5):
    lista1[c].append(ordem_dados[f'jogador{c}'])

aux = ''
for a in range(1, 5):
    for c in range(a+1, 5):
        if lista1[a][1] < lista1[c][1]:
            aux = lista1[c]
            lista1[c] = lista1[a]
            lista1[a] = aux
print()
print()
for c in range(1, 5):
    print(f"{c}º Lugar {lista1[c][0]} {lista1[c][1]}")




