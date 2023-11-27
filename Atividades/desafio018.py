print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 018\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{' MEDIA ALUNO' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
verdadeiro = True

num = 0
soma = 0


while verdadeiro:
    num += 1
    if num <= 1:
        aluno = str(input("Seu nome: "))
        print(f"\033[4m{'-' * 20}\033[0m")
        print(f"\033[32m{' MEDIA' :^20}\033[0m")
        print()
    numero = int(input(f"{' ' *4}{num}º Nota: "))
    soma += numero
    media = soma / num
    if num >= 5:
        print(f"\033[4m{'-' * 20}\033[0m")
        print(f"Media de {aluno}: {media}")
        resp = str(input("Quer continuar: ")).lower().strip()
        if resp[0] == "s":
            num = 0
        if resp[0] == "n":
            verdadeiro = False

