import math
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 33\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CONDIÇÃO COMPOSTA' :^32}\033[0m")
print(f"{'MAIOR E MENOR':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
num1 = int(input("1° numero: "))
num2 = int(input("2º numero: "))
num3 = int(input("3º numero: "))
menor = 0
maior = 0
if num1 > num2 > num3:
    maior = num1
    print(f"o maior numero é {maior}")
elif num2 > num1 > num3:
    maior = num2
    print(f"o maior numero é {maior}")
elif num3 >num2 > num1:
    maior = num3
    print(f"o maior numero é {maior}")

if num1 < num2 < num3:
    menor = num1
    print(f"o menor numero é {menor}")
elif num2 < num1 < num3:
    menor = num2
    print(f"o menor numero é {menor}")
elif num3 < num2 < num1:
    menor = num3
    print(f"o menor numero é {menor}")

#maior = max(num1, num2, num3)
#menor = min(num1, num2, num3)
#print(f"O maior numero é {maior}")
#print(f"o menor numero é {menor}")
