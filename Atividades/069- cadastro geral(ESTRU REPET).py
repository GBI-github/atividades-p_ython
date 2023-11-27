print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 69 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'CADASTRO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
soma = 0
soma1 = 0
soma2 = 0
outro = []
while True:

    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    print(f"\033[4;37m{'-' * 32}\033[0m")

    print(f"{'SEXO':^32}")
    print("[1]- FEMININO\n"
          "[2]- MASCULINO\n"
          "[3]- OUTROS\n")
    sex = int(input("Opção: "))
    print(f"\033[4;37m{'-' * 32}\033[0m")
    if sex == 1 and idade < 20:
        soma1 += 1
    if idade > 18:
        soma += 1
    if sex == 2:
        soma2 += 1
    if sex == 3:
        sex1 = str(input("Qual: "))
        outro.append(sex1)
    esc = str(input("Quer continuar[S/N]: ")).lower().strip()
    print()
    if esc[0] == "n":
        break
    print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"{'INFORMAÇÕES DE CADASTRO':^32}")
print()
print(f"18+: {soma}")
print(f"FEMININO -20: {soma1}")
print(f"MASCULINO: {soma2}")
for n in range(0, len(outro)):
    print(f"OUTROS: {outro[n]}", end=',')
print()
print(f"\033[4;37m{'-' * 32}\033[0m")


