print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 52\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'NUMERO PRIMO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
total = 0
num = int(input("Informe um numero: "))
for contador in range(1, num + 1):
    if num % contador == 0:
        print(f"\033[33m", end='')
        total = total + 1
    else:
        print("\033[31m", end='')
    print(f"{contador} ", end='')
print()
print(f"\n\033[m O numero {num} foi divizivel {total} vezes ")
print()
if total == 2:
    print("\033[32m Numero primo")
else:
    print("\033[31m Não é um numero primo")
