print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 77 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'TUPLAS' :^32}\033[0m")
print(f"{'CONTANDO VOGAIS':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
vogais = ["a", "e", "i", "o", "u"]
while True:
    palavra = str(input("Digite uma palavra: "))
    letra = "a"
    print(f"na palavra {palavra.upper()} temos: ", end='')
    for c in vogais:
        if any(l == c for l in palavra):
            print(c, end=', ')
    cont = str(input("\nQuer continuar? [S/N]: ")).lower().strip()
    if cont[0] == "n":
        break
