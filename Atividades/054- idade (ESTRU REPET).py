print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 54\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'MAIORIDADE':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
maiornome = []
totalmaior = 0

for contador in range(1, 3):
    idade = int(input("idade: "))
    nome = str(input("Nome: "))
    if idade >= 18:
        totalmaior = totalmaior + 1
        maiornome.append(nome)
print(f"tem {totalmaior} pessoas maiores de idade ")
print(f"Nomes: ")

for nome in maiornome:
    print("-",nome)
