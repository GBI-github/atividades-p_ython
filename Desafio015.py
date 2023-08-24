print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 015\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'soma de 1 a 100' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"{'VAMOS somar?' :^32}")
n = 1
cont = 0
cont1 = 0
while n != 0:
    n = int(input("Digite o valor: "))
    if n != 0:
        if n % 2 == 0:
            cont = cont + 1
        else:
            cont1 = cont1 + 1
print(f"Valores pares {cont}")
print(f"Valores impares {cont1}")
