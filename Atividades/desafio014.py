print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 014\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"{'MAIOR NUMERO' :^32}")
maior = 0
for contador in range(1, 999999999):
    num = int(input(f"{contador}° numero: "))
    escolha = str(input("Quer continuar [S/N]: ")).lower()
    if maior < num:
        maior = num
    if escolha == "n":
        break
print("Maior numero ", maior)

