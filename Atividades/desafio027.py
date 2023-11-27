print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 027\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
mercado = ("","coca-cola",
           "pão",
           "leite",
           "maçãs",
           "arroz",
           "feijão",
           "carne",
           "batata",
           "cenoura",
           "banana")
for c in range(1, len(mercado)):
    print(f"{c}.{mercado[c]}")