print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 30\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CONDIÇÃO COMPOSTA' :^32}\033[0m")
print(f"{'PAR OU INPAR':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
numero = int(input("Informe um numeo: "))
if numero % 2 == 0:
    print('PAR')
else:
    print('IMPAR')