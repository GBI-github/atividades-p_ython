print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 55\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'MAIOR PESO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
maiorpeso = 0
maiornome = ""
for contadoor in range(0, 2):
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    print()
    if peso > maiorpeso:
        maiorpeso = peso
        maiornome = nome


print(f"a pessoa mais pesada é: {maiornome}")
print(f"com: {maiorpeso}Kg")
