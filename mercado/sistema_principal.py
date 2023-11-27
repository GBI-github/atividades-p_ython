from dados_gerais.arquivo import *

while True:
    cabecalho("MERCADO JOíAS")
    escolha = menu(["Repor", "adicionar", "Comprar", "Revisar", "Sair"])
    if escolha == 1:
        try:
            senha = senha()
            if senha:
                produto = produtoexiste("Nome do Produto: ")  # ok
                if produto:  # ok
                    preco_novo = leiafloat("Novo Preço: R$")
                    novopreco(produto, preco_novo)
                    break
                else:
                    continue
            else:
                print()
                print("\033[31mERROR acesso negado!!\033[0m")
            escolha = 0
            continue
        except:
            break


