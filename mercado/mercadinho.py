from dados_gerais.arquivo import *

while True:
    cabecalho("MERCADO JOíAS")
    escolha = menu(["Comprar", "Sair"])
    if escolha == 1:
        cabecalho("PRODUTOS")
        produto()
        esc = menu(["Comprar Produto", "Sair"])
        if esc == 1:
            produto = produtoexiste("Nome do produto: ")
            if produto:
               cabecalho("CARRINHO")
               total = somapreco(produto)

            else:
                print()
                print(f"\033[31m{'Produto indisponível ou inexistente':^42}\033[0m")
                break
        if esc == 2:
            break
    if escolha == 2:
        break