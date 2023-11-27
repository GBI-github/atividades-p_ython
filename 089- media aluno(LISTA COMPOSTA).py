print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 89 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA COMPOSTA' :^32}\033[0m")
print()
print(f"\033[32m{'TIRANDO MEDIA':^29}\033[0m")
lista_media = []
media_individual = []
esc = "s"
c = 0
nome_usuarios = []
while esc[0] != "n":
    usuario = str(input("Nome: "))
    not1 = int(input("1º Nota: "))
    not2 = int(input("2º Nota: "))
    media = (not1 + not2) / 2
    dados_pessoais = [usuario, media]
    lista_media.append(dados_pessoais)
    del media_individual[0:]
    esc = str(input("Quer continuar[S/N]: ")).strip().lower()
    nome_usuarios.append(usuario)
    if esc[0] == "n":
        print(f"\033[32m{f'ALUNOS REGISTRADOS:':^32}\033[0m")
        for c in nome_usuarios:
            print(c)
        print(f"{'-' * 32}")

while True:
    mot = str(input("Visualizar Nota? [S/N]:")).strip().lower()
    print()
    if mot[0] == "n":
        break
    name = str(input("Nome: "))
    for c in range(0, len(lista_media)):
        for a in range(0, len(lista_media[c])):
            if lista_media[c][a] == name:
                print("Nota:", lista_media[c][1])
