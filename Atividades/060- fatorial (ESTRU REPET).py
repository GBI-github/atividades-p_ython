import math
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 60 \033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'FATORIAL':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
while True:
    num1 = int(input("Informe um numero: "))
    num = math.factorial(num1)
    print(f"Fatorial de {num1}! = {num}")
    print()
    esc = str(input("Quer continuar [N/S]: ")).lower().strip()
    if esc[0] == "n":
        break