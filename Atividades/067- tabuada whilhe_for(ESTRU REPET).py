print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 67 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'TABUADA WHILE[FOR]':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
while True:
    tabuada = int(input("Tabuada de qual valor: "))
    print(f"{'-' * 14}")

    for n in range(1, 10+1):
        print(f"{tabuada} X {n} = {tabuada * n}")

    print(f"{'-' * 14}")
    escolha = str(input("Quer continuar? [S/N]: ")).lower().strip()
    if escolha[0] == 'n':
        break
