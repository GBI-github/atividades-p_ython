print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 036\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DICIONARIO':^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
dados_jogador = dict()
gols_feitos = list()
historico_dos_jogadores = list()
while True:
    dados_jogador['nome'] = str(input("Nome do Jogador: ")).capitalize()
    quantas_partidas = int(input(f"Quantas partidas {dados_jogador['nome']} Jogou? "))
    for partidas in range(0, quantas_partidas):
        gols_feitos.append(int(input(f"Na {partidas}º Partida Gols Feito: ")))
    dados_jogador["gols"] = gols_feitos[:]
    dados_jogador["total"] = sum(gols_feitos[:])
    historico_dos_jogadores.append(dados_jogador.copy())
    dados_jogador.clear()
    gols_feitos.clear()
    while True:
        conti = str(input("Quer Continuar? [S/N]: ")).strip().lower()[0]
        if conti in "sn":
            break
    if conti == "n":
        break

for contagem_numerica, dicionario_historico in enumerate(historico_dos_jogadores):
    print(f'{contagem_numerica:>3} ', end="")
    for informacoes in dicionario_historico.values():
        print(f'{str(informacoes):<15}', end="")
    print()



