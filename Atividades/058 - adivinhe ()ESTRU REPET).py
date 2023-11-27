import random

print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 58\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'ADIVINHE O NUMERO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
chance = 0
while True:
    num_aleatorio = random.randint(0, 10)
    num = int(input("Informe um numero [0 a 10]: "))
    chance = chance + 1
    if num == num_aleatorio:
        print("Acertou")
        break
    escolha = str(input("Errou quer tentar de novo?[S/N]")).strip().lower()
    if escolha[0] == "n":
        break

print(f"Fim do programa, {chance} palpite(s)")