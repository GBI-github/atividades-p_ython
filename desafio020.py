print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 020\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
verdadeiro = True
num = 0
for n in range(0, 5):
    num += 1
    if num == 1:
        print(f"\033[31m{' * ' * num}\033[37m")
    elif num > 1:
        print(f"{' * ' * num}")

