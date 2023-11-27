print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 48\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'MULTIPLO DE 3':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
for contador in range(1, 501):
    if contador % 3 == 0:
        print(contador)