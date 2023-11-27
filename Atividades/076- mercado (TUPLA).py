print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 76 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'TUPLAS' :^32}\033[0m")
print(f"{'MERCADO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()

mercado = ("coca-cola", "2.50",
           "pão", "1.00",
           "leite", "3.50",
           "maçãs", "2.00",
           "arroz", "5.00",
           "feijão", "4.00",
           "carne", "10.00",
           "batata", "1.50",
           "cenoura", "1.00",
           "banana", "0.50")
soma = 0
men = ''
while True:
    item = mercado[soma]
    print(item.ljust(20, '.'), mercado[soma + 1])
    soma += 2
    if soma == 20:
        break
