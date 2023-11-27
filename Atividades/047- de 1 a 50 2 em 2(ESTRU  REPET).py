print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 47\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'DE 0 A 50':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
for contador in range(1, 51):
    if contador % 2 == 0:
        print(contador)
