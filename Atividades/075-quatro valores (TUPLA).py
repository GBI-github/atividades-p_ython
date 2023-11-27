print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 75 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'TUPLAS' :^32}\033[0m")
print(f"{'QUATRO VALORES':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
sequencia = ['', ]
pares = []
for c in range(1, 5):
    num = int(input(f"{c}º Numero: "))
    sequencia.append(num)
    if num % 2 == 0:
        pares.append(num)
soma = 0
tup = tuple(sequencia)
for c in tup:
    if c == 3:
        print("3 na ", tup.index(3), "º Posição")
    if c == 9:
        soma += 1
if soma >= 1:
    if soma > 1:
        print(f"o 9 aparece {soma} vezes")
    if soma == 1:
        print(f"o 9 aparece {soma} vez")

if pares:
    print(f"Números pares {tuple(pares)}")
