import random

print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 68 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'PAR OU IMPAR':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
soma = 0
soma1 = 0
while True:
    esc = str(input("PAR OU IMPAR?: ")).lower().strip()
    valor = int(input("Valor [0/10]: "))
    print()
    escolha = random.randint(0, 10)
    print(f"\033[32m{'RESULTADO' :^32}\033[0m")
    print(f"\033[4;37m{'-' * 32}\033[0m")
    print()
    v = escolha + valor
    print(v)
    if v % 2 == 0:
        valor1 = "par"
    elif v % 2 != 0:
        valor1 = "impar"

    print(valor1)

    if esc == valor1:
        vit = "Você Ganhou"
        print(vit)
    else:
        perd = "Você Perdeu"
        print(perd)

    if esc != valor1:
        soma = soma + 1
    if esc == valor1:
        soma1 = soma1 + 1
    print(f"\033[4;37m{'-' * 32}\033[0m")
    op = str(input("Quer continuar? [S/N]: ")).lower().strip()
    print()
    if op[0] == "n":
        break
print()
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'FIM DE GAME' :^32}\033[0m")
print()
print(f"Você Ganhou um total de {soma1} vez(es)")
print(f"Você Perdeu um total de {soma } vez(es)")
print()
print(f"\033[4;37m{'-' * 32}\033[0m")
