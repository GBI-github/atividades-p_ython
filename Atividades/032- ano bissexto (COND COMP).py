import calendar
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 32\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CONDIÇÃO COMPOSTA' :^32}\033[0m")
print(f"{'ANO BISSEXTO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
ano = int(input("Informe um ano: "))
bissexto = calendar.isleap(ano)
if bissexto == True:
    print("é um ano bissexto")
else:
    print("Não é um ano bissexto ")
