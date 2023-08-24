import random

print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 74 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'TUPLAS' :^32}\033[0m")
print(f"{'NÚMEROS ALEATÓRIOS':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
sec_num = []
maior = 0
menor = float("inf")
for n in range(0, 5):
    num_ale = random.randint(0, 100000)
    sec_num.append(num_ale)
    if num_ale > maior:
        maior = num_ale
    if num_ale < menor:
        menor = num_ale


print(tuple(sec_num))
print()
print(f"Maior numero {maior}")
print(f"Menor numero {menor}")
print(f"\033[4;37m{'-' * 32}\033[0m")