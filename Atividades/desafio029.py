print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 029\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'NÚMEROS AO QUADRADO' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(numeros)
num = []
for c in numeros:
    num.append(c**2)
print()
print("números ao quadrado\n")
print(tuple(num))
