print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 79 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA' :^32}\033[0m")
print(f"{'POSIÇÃO DOS NUMEROS':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
lista = []
num = int(input("Informe um numero [0]-EXIT: "))
lista.append(num)
while num != 0:
    num = int(input("Informe um numero [0]-EXIT: "))
    for c in lista:
        if num != c:
            numero = num[:]
    if num != 0:
        lista.append(numero)
lista.sort()
print("Esses valores ordenados ficam: ", end='')
for c in lista:
    print(c, end=', ')
