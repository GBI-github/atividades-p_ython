print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 78 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA' :^32}\033[0m")
print(f"{'MAIOR,MENOR,POSIÇÃO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()

while True:
    lista = ["", ]
    maior = 0
    menor = float("inf")
    for c in range(1, 6):
        num = int(input(f"{c}- valor: "))
        lista.append(num)
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    print(lista[1:])
    print(f"Maior numero: {maior}")
    print(f"Menor numero: {menor}")
    print(f"Maior na posição {lista.index(maior)}")
    print(f"Menor na posição {lista.index(menor)}")
    esc = str(input("Quer continuar [S/N]?: ")).strip().lower()
    if esc[0] == "n":
        break
