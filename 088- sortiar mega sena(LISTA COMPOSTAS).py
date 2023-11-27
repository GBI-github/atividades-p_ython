print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 88 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA COMPOSTA' :^32}\033[0m")
print()
print("=-" * 15, end="=\n")
print(f"\033[32m{'JOGO DA MEGA SENA':^29}\033[0m")
print()
from random import randint

lista_numeros = []
lista = []
while True:
    num = int(input(" Quantas Jogos?: "))
    for a in range(0, num):
        for n in range(0, 6):
            e = randint(0, 60)
            if any(numero == e for numero in lista):
                while True:
                    e = randint(0, 60)
                    if any(numero != e for numero in lista):
                        lista.append(e)
                        break
            else:
                lista.append(e)
        lista_numeros.append(lista[:])
        del lista[0:]
    break
num1 = 0
lista_numeros.sort()
for a in range(0, num):
    num1 += 1
    num2 = 0
    print(f"\nJogo {num1}: ", end='[')
    for c in lista_numeros[a]:
        print(c, end="")
        if num2 < 5:
           print(",", end=" ")
        num2 += 1
    print("]", end="")
print()
print("=-" * 15, end="=\n")