print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 66 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'FLAG 999[PARADA]':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
num1 = 0
soma = 0
while True:
    num1 = num1 + 1
    num = int(input(f"{num1}º Numero: "))
    if num == 999:
        break
    soma += num

print(f"\033[32m{'SOMA' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
print(f"{soma:^32} ")
print()
print(f"\033[4;37m{'-' * 32}\033[0m")
