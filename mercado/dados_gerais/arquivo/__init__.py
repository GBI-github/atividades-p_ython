from mercado.dados_gerais.interface import *
from time import sleep


def senha():
    try:
        b = leiaint("Senha: ")
        print("passou")
        with open('funcionario', 'r') as sennha:
            for c in sennha:
                dados = int(c)
                if b == int(dados):
                    return True
                else:
                    return False
    except TypeError:
        print("\033[31mERROR ao achar funcionário")
        return False


def produtoexiste(mensagem):
    a = str(input(mensagem)).lower()
    try:
        with open("produtos", 'r') as produtos:
            produtos_linha = produtos.readlines()
        for c in produtos_linha:
            partes = c.strip().split("-")
            nome_produto = partes[0].strip()
            if nome_produto == a:
                return nome_produto
        if nome_produto != a:
            return False
    except:
        print("error")


def novopreco(p, n_p):
    a = n_p
    b = p
    print(b)
    try:
        with open("produtos", 'r') as produtos:
            produtos_linha = produtos.readlines()
        lista_produto = list()
        for c in produtos_linha:
            partes = c.strip().split("-")

            if b == partes[0]:
                partes[1] = conversor(a)
            novos_produtos = "-".join(partes)
            lista_produto.append(novos_produtos)
        with open("produtos", "w") as produtos:
            produtos.writelines("\n".join(lista_produto))
    except:
        print("Error ao achar produto")
    else:
        return True


def produto():
    with open('produtos', 'r') as produtos:
        produtos1 = produtos.readlines()
        a = 1
        for c in produtos1:
            partes = c.strip().split("-")
            print(f"{partes[0]:.<34}{partes[1]:}")
            a = a + 1
        sleep(2)
        print()


def carrinho(nome, quant):
    print("ok")





