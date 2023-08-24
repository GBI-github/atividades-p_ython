print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 49\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'TABUADA':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
inf = int(input("Numero: "))
print()
for contador in range(1, 11):
    print(f"{inf} X {contador} = {inf* contador} ")
