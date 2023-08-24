from random import randint
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 28\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CONDIÇÃO COMPOSTA' :^32}\033[0m")
print(f"{'ACERTAR NUMERO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
aleatorio = int(randint(0,5))
numero = int(input("Digite um numero entre (0 a 5): "))
if numero == aleatorio:
    print("você acertou o numero que eu pensei")
else:
    print("tente novamente, você errou! ")
