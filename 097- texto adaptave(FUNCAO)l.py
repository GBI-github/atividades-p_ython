print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 97 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'FUNÇÃO DEF' :^32}\033[0m")
print()
print(f"\033[32m{'TEXTO ADAPTÁVEL':^32}\033[0m")
print()


def escreva(txt):
    print("-" * len(txt))
    print(txt.capitalize())
    print("-" * len(txt))


texto = str(input("Escreva um texto: "))
escreva(texto)
