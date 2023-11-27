print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 99 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'FUNÇÃO DEF' :^32}\033[0m")
print()
print(f"\033[32m{'MAIOR NÚMERO':^32}\033[0m")
print()

from time import sleep


def numeros(*numero):
    print('-=' * 25)
    print('Analisando os valores passados...')

    for c in numero:
        print(c, end=" ")
        sleep(0.3)
    print(f"foram informados ao todo {len(numero)} numeros")
    print('O maio numero informado foi ', max(numero))


numeros(1, 7, 5, 9, 2, 6, 8)
numeros(0)
numeros(0, 3, 5, 121, 4, 6, 7, 2, 4, 3, 7, 3)
