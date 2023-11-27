import random
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 016\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{' DE 1 A 100' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"{'ADIVINHE O NUMERO!!!?' :^32}")
num_aleatorio = random.randint(1, 100)
print(num_aleatorio)
while True:
    num = int(input("Numero: "))
    if num > num_aleatorio:
        print("MENOS")
    if num < num_aleatorio:
        print("MAIS")
    if num == num_aleatorio:
        break

print("Você acertou!, PARABENS!! ")
