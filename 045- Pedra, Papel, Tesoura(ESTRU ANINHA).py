from random import randint
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 45\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA ANINHADA' :^32}\033[0m")
print(f"{'JÓ KEN PÔ':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print("Pedra, Papel, Tesoura")
escolha = str(input("Sua escolha: ")).lower()
escolha_aleatoria = randint(1,3)
if escolha_aleatoria == 1:
    escolha_aleatoria = "papel"
    print(f"Maquina: {escolha_aleatoria}")
elif escolha_aleatoria == 2:
    escolha_aleatoria = "pedra"
    print(f"Maquina: {escolha_aleatoria}")
elif escolha_aleatoria == 3:
    escolha_aleatoria = "tesoura"
    print(f"Maquina: {escolha_aleatoria}")
if escolha == "papel" and escolha_aleatoria == "tesoura":
    print("Eu venci")
elif escolha == "tesoura" and escolha_aleatoria == "papel":
    print("Voce venceu")
elif escolha == "papel" and escolha_aleatoria == "papel":
    print("empate")
if escolha == "pedra" and escolha_aleatoria == "papel":
    print("Eu venci")
elif escolha == "papel" and escolha_aleatoria == "pedra":
    print("Voce venceu")
elif escolha == "pedra" and escolha_aleatoria == "pedra":
    print("empate")
if escolha == "tesoura" and escolha_aleatoria == "pedra":
    print("Eu venci")
elif escolha == "pedra" and escolha_aleatoria == "tesoura":
    print("Voce venceu")
elif escolha == "tesoura" and escolha_aleatoria == "tesoura":
    print("empate")




