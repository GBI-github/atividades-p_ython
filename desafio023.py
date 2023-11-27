print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 023\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CALENDARIO' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
calendario = ("", 'janeiro', 'fevereiro', 'março', 'maio', 'abril', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
              'novembro',
              'dezembro')
usuario = 1
print("\033[0;31mEXIT[0] \033[0m ")
while usuario != 0:
    usuario = int(input("Mês[1 a 12]: "))
    if usuario <= 12:
        print(calendario[usuario])
