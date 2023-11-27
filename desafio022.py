print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 022\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'NUMEROS PARES' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_pares = 0

for numero in range(len(numeros)):

    if numero % 2 != 0:
        continue
    soma_pares += numero

print(soma_pares)

