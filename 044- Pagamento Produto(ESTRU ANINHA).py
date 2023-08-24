print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 44\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA ANINHADA' :^32}\033[0m")
print(f"{'COMPRA':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
compra = float(input("Preço do produto: R$"))
print(f"{'FORMA DE PAGAMENTO':^32}")
print("[1]- A vista\n"
      "[2]- Cartão a Vista\n"
      "[3]- 2X Cartão \n"
      "[4]- 3x ou + Cartão\n")
metodo_pagamento = int(input("Qual a forma de pagamento: "))
if metodo_pagamento == 1:
    desconto = (compra * 10)/100
    print(f"pagamento Total: R${compra-desconto}")
elif metodo_pagamento == 2:
    desconto = (compra * 5) / 100
    print(f"pagamento Total: R${compra - desconto}")
elif metodo_pagamento == 3:
    print(f"pagamento Total: R${compra}")
elif metodo_pagamento == 4:
    desconto = (compra * 20) / 100
    print(f"pagamento Total: R${compra + desconto}")
