from math import trunc
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 16\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'BLIBLIOTECA MATH' :^32}\033[0m")
print(f"{'NUMERO INTEIRO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
num = float(input("Informe um numero real: "))
print(f"a porçao inteira desse numero é {trunc(num)}")