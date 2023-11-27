print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 028\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA PREÇO' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
preco = (1_000, 7_500, 8_500, 7_830,)
maior = 0
menor = float("inf")
for c in preco:
    if c > maior:
        maior = c
    if c < menor:
        menor = c

print(f"R${maior:,.0f}".replace(",", "."))
print(f"R${menor:,.0f}".replace(",", "."))
