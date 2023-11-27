print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 037\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DICIONARIO E FUNCAO':^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")


def alfabeto(frase):
    letras = [chr(ord('a') + i) for i in range(26)]
    dicionario_letras = dict()
    soma = 0
    for c in letras:
        a = frase.count(c)
        dicionario_letras[c] = a

    for k,v in dicionario_letras.items():
        print("-=" * 12)
        print(f"letra {k} apareceu {v} vezes")
        print()


def continuar():

    cont = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    return cont == 'S'


while True:
    texto = str(input("Digite uma frase: "))
    print()
    print()
    alfabeto(texto)
    if not continuar():
        break


