import numpy as np
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 62\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'PROGRESSÃO ARITIMETRICA':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
termo = int(input("Primeria termo: "))
razao = int(input("Razão: "))
ultimo = int(input(f"Ultimo numero > {termo}: "))
seq = []
seq2= []
while True:
    sequencia = np.arange(termo, razao + ultimo * termo, razao)
    seq = sequencia
    break
seq1 = " → ".join(str(numero) for numero in seq[:10])
print(f"10 primeiras sequencias: {seq1} FIM")
soma = 10
while True:
    sequencia = np.arange(termo, razao + ultimo * termo, razao)
    seq2 = sequencia
    quant = int(input("Quantos termos voce quer ver digite[0] pra finalizar: "))
    soma = soma + quant
    seq1 = " → ".join(str(numero) for numero in seq2[:quant])
    print(f"{seq1}")
    if quant == 0:
        break
print(f"Foram mostradas {soma} termos")
