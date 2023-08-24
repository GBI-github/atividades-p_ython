print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 013\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'soma de 1 a 100' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"{'VAMOS somar?' :^32}")
soma = 0
for contador in range(1, 101):
    soma = soma + contador
print("soma total", soma)
    