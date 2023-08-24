print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 64\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'NUMEROS VARIADOS':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
print()
verdadeiro = True
print(f"\033[32m{'INFORME UM NUMERO: ' :^32}\033[0m")
soma = 0
while verdadeiro:
    print(f"\033[4;37m{'-' * 32}\033[0m")
    numero = int(input("SAIR[999]: "))

    if numero == 999:
        verdadeiro = False
    else:
        soma = soma + numero

print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"soma igual a: {soma}")

