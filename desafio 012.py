print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 012\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CONTAGEM' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"{'VAMOS CONTAS DE 2 EM 2?' :^32}")
for contador in range(1,22):
    if contador %2 == 0:
        print(contador)
