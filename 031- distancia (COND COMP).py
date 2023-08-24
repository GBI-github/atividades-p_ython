print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 31\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CONDIÇÃO COMPOSTA' :^32}\033[0m")
print(f"{'DISTANCIAMENTO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
passagem = int(input("Qual é a distancia de sua viajem Km: "))
if passagem == 200:
    print(f"Preço da passagem: R${passagem * 0.50}")
elif passagem > 200:
    print(f"Preço da passagem: R${passagem * 0.45}")
