import math, colorama
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 35\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CONDIÇÃO COMPOSTA' :^32}\033[0m")
print(f"{'TRIANGULO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
num1 = int(input("1° segmento: "))
num2 = int(input("2º segmento: "))
num3 = int(input("3º segmento: "))
if num1 + num2 > num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print("Da pra formar um triangulo")
else:
    print("Não da pra se formar um triangulo")
