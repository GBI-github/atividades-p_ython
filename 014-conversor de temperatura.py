print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 14\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CONVERSOR DE TEMPERATURA' :^32}\033[0m")
print(f"{'Cº > Fº':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
grau = float(input("informe a temperatura em Cº: "))
fire = grau * 1.8 + 32
print(f"A temperatura de {grau}°C correspnde a {fire}°F!")
