print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 82 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA' :^32}\033[0m")
print(f"{'PAR, IMPAR LISTA':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[0;31m Fechar o programa DIGITE- 0\033[0m")
lista = []
lista1 = []
lista2 = []
c = 0

while True:
    c += 1
    num = int(input(f"{c}º valor"))
    lista.append(num)
    if num % 2 == 0:
        lista1.append(num)
    elif num % 2 != 0:
        lista2.append(num)
    if num == 0:
        break
print("Total de números:")
print(len(lista))
print("Números pares:")
print("   ",lista1)
print("Números impares:")
print("   ",lista2)

