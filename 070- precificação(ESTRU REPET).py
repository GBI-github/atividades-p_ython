print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 70 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'PRECIFICAÇÃO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
soma = 0
soma1 = 0
menor_barato = float('inf')
nome = ''
while True:
    nome_produto = str(input("Nome do Produto: "))
    preco_produto = float(input("Preço: "))
    soma += preco_produto
    if preco_produto > 1000:
        soma1 += 1
    if preco_produto < menor_barato:
        menor_barato = preco_produto
        nome = nome_produto
    cont = str(input("Quer continuar? [S/N]: ")).lower().strip()
    if cont[0] == "n":
        break
print(f"Total Gasto: R${soma}")
print(f"Produtos acima de R$1000: {soma1}")
print(f"Produto mais barato: {nome.title()}")

