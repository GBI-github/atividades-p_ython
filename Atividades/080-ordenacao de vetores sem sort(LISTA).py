print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 80 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA' :^32}\033[0m")
print(f"{'ORDENANDO VALORES':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
lista = []
aux = 0
for c in range(1, 6):
    num = int(input(f"{c}º Valor: "))
    lista.append(num)

for c in range(0, len(lista)):
    for j in range(c+1, len(lista)):
        if lista[c] > lista[j]:
            aux = lista[c]
            lista[c] = lista[j]
            lista[j] = aux
print(lista)
