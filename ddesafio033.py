print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 033\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DUPLA LISTA' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")

dados_produtos = []
while True:
    nome = str(input("Nome do produto: "))
    preço = float(input("Preço do produto: "))
    stock = int(input("Quantidade em stock: "))
    produtos = nome, preço, stock
    dados_produtos.append(produtos)
    esc = str(input("Continuar Registro? [S/N]: ")).strip().lower()[0]
    if esc == "n":
        break
lista = ["Nome: ", "Preço: ","Stock: "]
for c in range(0, len(dados_produtos)):
    print()
    for a in range(0, len(dados_produtos[c])):
        print(lista[a])
        print(dados_produtos[c][a], " "*10, end='')

