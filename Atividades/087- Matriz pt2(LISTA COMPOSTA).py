print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 87 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA COMPOSTA-LISTAS DUPLAS' :^32}\033[0m")
print()
print(f"\033[32m{'MATRIZ PT-2':^32}\033[0m")
lista = [[], [], []]

for c in range(0, 3):
    for a in range(0, 3):
        num = int(input(f"[{c},{a}]: "))
        lista[c].append(num)
soma = 0
soma1 = 0
maior = 0
print()
print(f"\033[32m{'MATRIX 3X3'}\033[0m")
for c in range(0, 3):
    for a in range(0, 3):
        print(f"[{lista[c][a]:^5}]", end='')
        if lista[c][a] % 2 == 0:
            soma += lista[c][a]
        if lista[c][a] == lista[c][2]:
            soma1 += lista[c][a]
        if lista[1][a] > maior:
            maior = lista[1][a]
    print()
print()
print()
print(f"A soma de todos os pares é {soma}")
print(f"A soma dos números da 3º coluno é {soma1}")
print(f"Maior numero da 2º linha {maior}")

