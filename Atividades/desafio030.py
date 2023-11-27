print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 030\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'REMOVER ELEMENTO LISTA' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")

nomes = ["Alice", "Bob", "Charlie", "gabriel"]
elemento_remove = "gabriel"
nome = 1
while nome != '0':
    nome = str(input("Nome [0]: "))
    if nome != "0":
        nomes.append(nome)
print(nomes)
while elemento_remove in nomes:
    nomes.remove(elemento_remove)
print(nomes)
