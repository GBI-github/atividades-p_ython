print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 96 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'FUNÇÃO DEF' :^32}\033[0m")
print()
print(f"\033[32m{'TAMANHO DA AREA':^32}\033[0m")
print()


def tamanho(a, b):
   tam = l * c
   print(f"Á área de um terreno {l}X{c} é de {tam}m²")


l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
tamanho(l, c)
