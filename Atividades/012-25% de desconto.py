print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 12\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'PORCENTAGEM' :^32}\033[0m")
print(f"{'25% DE DESCONTO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
produto = str(input("o que voce deseja comprar?: "))
preço = float(input(f"Qual é o preço do(a) {produto}?:R$"))
desconto = (25 * preço)/100
print(f"o novo preço a ser pago é {preço - desconto}R$")