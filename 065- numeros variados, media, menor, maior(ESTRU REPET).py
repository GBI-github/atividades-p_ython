print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 65033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'NUMEROS VARIADOS[ADICIONAL]':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
print()
meno_num = 0
maior_num = 0
verdadeiro = True
print(f"\033[32m{'INFORME UM NUMERO: ' :^32}\033[0m")
soma = 0
quant = 0
while verdadeiro:
    print(f"\033[4;37m{'-' * 32}\033[0m")
    numero = int(input("SAIR[999]: "))

    if numero == 999:
        verdadeiro = False

    elif numero != 999:
        soma = soma + numero
        quant = quant + 1

        if maior_num < numero:
            maior_num = numero
        if maior_num > numero:
            menor_num = numero

print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"soma igual a: {soma}")
print(f"a media é igual {soma/quant:.2f}")
print(f"Maior numero: {maior_num}")
print(f"Menor numero: {menor_num}")
