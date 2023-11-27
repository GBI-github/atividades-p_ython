print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 57\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'INFORMAÇÕES PESSOAIS':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
verdadeiro1 = True
while verdadeiro1:
    print()
    nome = str(input("Informe seu nome COMPLETO: "))
    while True:
        sexo = str(input("Seu sexo [F/M]: ")).strip().lower()
        if sexo[0] == "f" or sexo[0] == "m":
            break
        else:
            print("Erro, informe novamente")

    idade = int(input("Ano de Nascimento: "))
    idade = 2023 - idade
    naci = str(input("Nacionalidade: "))

    print("Estado civil")

    verdade = True
    while verdade:
        print("[1]- Solteiro\n"
              "[2]- Casado\n"
              "[3]- Divorciado\n"
              "[4]- Viúvo\n"
              "[5]- Namorando\n")
        estado = int(input("Opção: "))
        lista = [" ", "Solteiro", "Casado", "Divorciado", "viúvo", "Namorando"]
        if estado < 6:
            verdade = False

    if sexo == "f":
        sexo = "feminino"
    elif sexo == "m":
        sexo = "masculino"

    print(f"Nome: {nome.upper()} {' ' * 3}Sexo: {sexo.upper()}\n"
          f"Idade: {idade} anos\n"
          f"Nacionalidade: {naci.upper()}\n"
          f"Estado Civil: {lista[estado].upper()} ")
    print()
    reg = str(input("Esta tudo CORRETO? [S/N]: ")).lower().strip()
    if reg[0] == "s":
        verdadeiro1 = False

print("Registrado")
print()

