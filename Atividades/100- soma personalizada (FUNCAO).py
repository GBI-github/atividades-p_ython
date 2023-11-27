import random

print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 100 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'FUNÇÃO DEF' :^32}\033[0m")
print()
print(f"\033[32m{'SOMA PERSONALIZADA':^32}\033[0m")
print()
from random import randint
from time import sleep
numeros = []


def sorteio():
    for c in range(0, 5):
        a = random.randint(0, 100)
        numeros.append(a)

    print("numeros sorteados: ", end='')
    for c in numeros:
        print(c, end=' ')
        sleep(0.5)
    print()


sorteio()


def par():
    soma = 0
    for c in range(len(numeros)):
        if numeros[c] % 2 == 0:
            soma += numeros[c]

    print('numeros pares:', end=' ')
    for c in range(len(numeros)):
        if numeros[c] % 2 == 0:
            print(numeros[c], end=' ')
        sleep(0.5)
    print()
    sleep(0.5)
    print("soma dos numeros pares", soma)


par()





