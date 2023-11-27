from mercado.dados_gerais.interface import *


def encontrar_linha(arquivo, produto):
    with open(arquivo, 'r') as produtos:
        linha_prod = produtos.readlines()
        for i, linnha in enumerate(linha_prod, 1):
            if produto in linnha:
                return i


def somapreco(nome_produto):
    b = "produtos"
    a = nome_produto
    l = encontrar_linha(b, a)
    a = open('produtos', 'rt')
    produtos = a.readlines()
    print(produtos)


prod = "alface"
somapreco(prod)