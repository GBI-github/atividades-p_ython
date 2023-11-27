from babel.numbers import format_currency


def aumentar(n, c=0, a=False):
    """ex 107- fiz os modulos
       ex 108- covertir os valores em moedas
       ex 109- criei um valor opcional 'a' """
    a = c * n / 100
    n = int(n + a)
    if a:
        d = format_currency(n, 'BRL', locale='pt_BR')
        return d
    return n


def metade(n, a=False):
    n = int(n / 2)
    if a:
        d = format_currency(n, 'BRL', locale='pt_BR')
        return d
    return n


def dobro(n, a=False):
    n = int(n * 2)
    if a:
        d = format_currency(n, 'BRL', locale='pt_BR')
        return d
    return n


def reduzindo(n, c=0, a=False):
    a = (c * n) / 100
    n = int(n - a)
    # 109
    if a:
        d = format_currency(n, 'BRL', locale='pt_BR')
        return d
    return n


def moeda(n):
    # 108
    n = int(n)
    d = format_currency(n, 'BRL', locale='pt_BR')
    return d


def resumo(a=0, b=0, c=0):
    d = format_currency(a, 'BRL', locale='pt_BR')
    print("_"*34)
    print(f"{'RESUMO DO VALOR':^34}")
    print("_" * 34)
    print(f"{'Preço Analisado:':<20}{d}")
    print(f"{'Dobro do Preço:':<20}{dobro(a, True)}")
    print(f"{'Metade do preço:':<20}{metade(a, True)}")
    print(f"{f'{b}% de aumento:':<20}{aumentar(a, b, True)}")
    print(f"{f'{c}% de redução:':<20}{reduzindo(a,c,True):}")
    print("_" * 34)