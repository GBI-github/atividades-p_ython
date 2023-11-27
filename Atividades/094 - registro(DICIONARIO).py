print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 94 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DICIONARIO' :^32}\033[0m")
print()
print(f"\033[32m{'REGISTRO':^32}\033[0m")
print()
registro_pessoal = dict()
registro_geral = list()
grupo_feminino = list()
soma = 0
while True:
    registro_pessoal['nome'] = str(input("Nome: "))
    registro_pessoal['sexo'] = str(input("sexo: ")).strip().lower()[0]
    registro_pessoal['idade'] = int(input('idade: '))
    soma = soma + registro_pessoal['idade']
    if registro_pessoal['sexo'] == "f":
        grupo_feminino.append(registro_pessoal['nome'])
    cont = str(input("Quer continuar? [S/N]")).lower().strip()[0]
    registro_geral.append(registro_pessoal.copy())
    registro_pessoal.clear()
    if cont == "n":
        break
print()
media = soma / len(registro_geral)
print(f"-O grupo tem {len(registro_geral)} pessoas.")
print(f"-A média de idade dentro do grupo é {media:.2f}")
if len(grupo_feminino) != 0:
    print(f"-As mulheres neste grupo são ", end='')
    for c in grupo_feminino:
        print(c, end=' ')
print()
print(F"-lista de pessoas acima da media: ")
print()
for c in range(0, len(registro_geral)):
    if registro_geral[c]['idade'] >= media:
        print(f"Nome= {registro_geral[c]['nome']}; Sexo={registro_geral[c]['sexo']}; "
              f"Idade= {registro_geral[c]['idade']}.")
print()
print("<<<ENCERRADO>>>")
