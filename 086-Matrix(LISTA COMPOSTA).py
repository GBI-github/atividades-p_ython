print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 86 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA COMPOSTA-LISTAS DUPLAS' :^32}\033[0m")
print()
print(f"\033[32m{'MATRIZ':^32}\033[0m")
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"[{linha},{coluna}] Valor:"))
print("-" * 32)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]}:^5]", end='')
    print()


