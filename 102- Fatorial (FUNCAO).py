print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 102 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'FUNÇÃO DEF' :^32}\033[0m")
print()
print(f"\033[32m{'FATORIAL':^32}\033[0m")
print()


def fatorial(num, show=False):
    """calcula o fatorial de um numero e retorna o resultado
        show = False nao retorna sequencia de multiplicação"""

    if not show:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f

    if show:
        c = 5
        while c >= 1:
            if c != 1:
                print(c, end=' x ')
                c -= 1
            if c == 1:
                print(c, end=' ')

                break
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f


a = 5

print(f"fatorial de {a} = {fatorial(a)}")



