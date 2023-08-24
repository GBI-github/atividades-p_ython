import random
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 19\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'BLIBLIOTECA RANDOM' :^32}\033[0m")
print(f"{'ESCOLHER ALUNO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
a1 = str(input("1º ALUNO: "))
a2 = str(input("2° ALUNO: "))
a3 = str(input("3° ALUNO: "))
a4= str(input("4º ALUNO: "))
lista= [a1,a2,a3,a4]
print(f"Quem vai limpar o quadro é o {random.choice(lista)}")
