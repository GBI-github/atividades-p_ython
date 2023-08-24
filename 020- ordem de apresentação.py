import random
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 20\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'BLIBLIOTECA RANDOM' :^32}\033[0m")
print(f"{'ORDEM DE APRESENTAÇÃO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
a1 = str(input("1º ALUNO: "))
a2 = str(input("2° ALUNO: "))
a3 = str(input("3° ALUNO: "))
a4 = str(input("4º ALUNO: "))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(f" a ordem de apresentação sera ", end=' ')
print(lista)
