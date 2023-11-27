print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 102 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'FUNÇÃO DEF' :^32}\033[0m")
print()
print(f"\033[32m{'FATORIAL':^32}\033[0m")
print()


def ficha(a, b):
    if a.strip() == '':
        a = "<desconhecido>"
    if b.isnumeric():
       b = int(b)
    else:
        b = 0
    print(f"Nome do jogador: {a.capitalize()}, quantidade de gols: {b}")


nome = str(input("Nome do jogador: "))
quant = input("Quantidade de gols: ")
ficha(nome, quant)
