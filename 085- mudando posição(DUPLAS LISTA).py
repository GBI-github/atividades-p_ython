print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 85 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DUPLA LISTA' :^32}\033[0m")
print()
numeros = list()
print()
print(f"\033[32m{'PARES E IMPARES':^32}\033[0m")
num = 0
for c in range(1, 6):
    numero = int(input(f"{c}º Numero: "))
    numeros.append(numero)

for c in numeros:
    if c % 2 == 0:
        num += 1

for c in range(0, len(numeros)):
    for j in range(c + 1, len(numeros)):
        if numeros[j] % 2 == 0:
            aux = numeros[c]
            numeros[c] = numeros[j]
            numeros[j] = aux
            
print("Numeros pares", sorted(numeros[0:num]))
print("Numeros impares", sorted(numeros[num:]))

