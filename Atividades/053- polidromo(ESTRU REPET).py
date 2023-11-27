print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 53\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'FRASE PALÍDROMO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
frase = str(input("Digite uma frase: ")).lower().strip()
frase = frase.replace(" ", "")

if frase == frase[::-1]:
    print("essa frase é um palídromo")
else:
    print("essa frase não é um palíndromo")