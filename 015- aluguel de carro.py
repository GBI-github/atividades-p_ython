print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 05\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'MATEMATICA BASICA' :^32}\033[0m")
print(f"{'ALUGUEL DE CARRO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
km = float(input("Quantos Km rodados?: "))
dias = int(input("Quantos dias rodados?: "))
custodia = dias * 60
custokm = km * 0.15
custototal = custokm + custodia
print()
print(f"total a pagar R${custototal}")
