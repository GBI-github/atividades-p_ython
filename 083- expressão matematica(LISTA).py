print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 83 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA' :^32}\033[0m")
print(f"{'EXPRESSÕES MATEMÁTICAS':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
lista = []
expre = str(input("Digite uma expressão que use parenteses: "))
cont = 0
cont1 = 0
lista.append(expre)
if expre[0] != "(":
    print("A expressão esta com erro nos parenteses")
else:
    for c in expre:
        if c == "(":
            cont += 1
        if c == ")":
            cont1 += 1
    if cont == cont1:
        print("Expressão correta")
    else:
        print("A expressão esta com erro nos parenteses")
