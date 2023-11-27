print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 98 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'FUNÇÃO DEF' :^32}\033[0m")
print()
print(f"\033[32m{'CONTADOR':^32}\033[0m")
print()
from time import sleep


def numero(n1, n2, n3):
    print('=-' * 15)
    print(f"Contagem de {n1} ate {n2} de {n3} em {n3}!")
    if n1 > n2:
        if n2 % 2 != 0:
            for c in range(n1, n2-1, -n3):
                print(c, end=' ')
                sleep(0.2)
            print("FIM")
        else:
            for c in range(n1, n2-2, -n3):
                print(c, end=' ')
                sleep(0.2)
            print("FIM")

    if n1 < n2:
        for c in range(n1, n2+1, abs(n3)):
            print(c, end=' ')
            sleep(0.2)
        print("FIM")


numero(1, 10, 1)
numero(10, 0, 2)
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
numero(inicio, fim, passo)



