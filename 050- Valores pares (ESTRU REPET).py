print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 50\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'SOMA PAR':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
soma = 0
for contador in range(1, 3):
    num = int(input("Numero: "))
    if num % 2 == 0:
        soma = soma + num
print(f"Valor dos numeros pares {soma}")
