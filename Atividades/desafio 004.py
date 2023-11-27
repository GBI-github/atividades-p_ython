print(f"{'-' * 10} DESAFIO 004 {'-' * 10}")
print(f"{'-' * 33}")
print(f"{'':^32}")
print(f"{'-' * 33}")
caractere = str(input("Me diga uma palavra: ")).strip()
palava1 = caractere[::-1]
print(f"È um pálidromo {palava1 in caractere}")