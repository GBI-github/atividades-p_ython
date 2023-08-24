print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 84 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DUPLA LISTA' :^32}\033[0m")

print(f"\033[4;37m{'-' * 32}\033[0m")
registro_pesado = list()
registro_leve = list()
soma = 0

import time

while True:
    print()
    print()
    print(f"\033[32m{'REGISTRO':^32}\033[0m")
    nome = str(input("Nome: ")).lower().strip()
    peso = float(input("Peso: "))
    registro = [nome, peso]
    if registro[1] > 70:
        registro_pesado.append(registro[:])

    if registro[1] <= 70:
        registro_leve.append(registro[:])
    del registro
    soma += 1
    cont = str(input("Continuar registro [S/N]: ")).lower().strip()
    if cont[0] == "n":
        # time.sleep(2)
        print()
        print()
        print(f"\033[31m{'REGISTRO FINALIZADO':^32}\033[0m")
        print(f"\033[4;37m{'-' * 32}\033[0m")
        break

    # time.sleep(2)
    print()
    print(f"\033[32m{'REGISTRO REALIZADO COM SUCESSO':^32}\033[0m")
    print()
    print(f"\033[4;37m{'-' * 32}\033[0m")
lista = ["nome: ", "peso: "]
print()
print(f"Quantidade de registro: {soma}")

maior = 0
pesados = []
menor = float("inf")
leves = []

for c in range(0, len(registro_pesado)):
    nome, numero = registro_pesado[c]
    if numero > maior:
        maior = numero
    if numero == maior:
        pesados.append(nome)

for c in range(0, len(registro_leve)):
    nome, numero = registro_leve[c]
    if numero < menor:
        menor = numero
    if numero == menor:
        leves.append(nome)

for c in range(0, len(registro_pesado)):
    print(f"\033[32m{f'{c + 1}º REGISTRO PESO [PESADO]:':^32}\033[0m")
    print()
    for j in range(0, (len(registro_pesado[c]))):
        print(lista[j], end='')
        print(registro_pesado[c][j], "Kg")
    print(f"{'-' * 32}")

for c in range(0, len(registro_leve)):
    print(f"\033[32m{f'{c + 1}º REGISTRO PESO [LEVE]:':^32}\033[0m")
    print()
    for j in range(0, (len(registro_leve[c]))):
        print(lista[j], end='')
        print(registro_leve[c][j], "Kg")
    print(f"{'-' * 32}")

if len(leves) > 0:
    print(f"os mais leves sao ", ', '.join(leves))
if len(pesados) > 0:
    print(f"os mais pesados sao ", ', '.join(pesados))
