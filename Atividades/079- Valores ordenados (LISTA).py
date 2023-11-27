print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 79 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA' :^32}\033[0m")
print(f"{'POSIÇÃO DOS NUMEROS':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
lista = []
numero = 0
while True:
    num = int(input("Informe um numero [0]-EXIT: "))
    if num not in lista:
        if num != 0:
            lista.append(num)
    if num == 0:
        break
lista.sort()
print("Esses valores ordenados ficam: ", end='')
for c in lista:
    print(c, end=', ')
