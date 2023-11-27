print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 95 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DICIONARIO' :^32}\033[0m")
print()
print(f"\033[32m{'RENDIMENTO DOS JOGADORES':^32}\033[0m")
print()
historico_jogador = dict()
registro_jogadores = list()
gols_jogos = list()

while True:
    historico_jogador.clear()
    print('_'*27)
    historico_jogador['nome'] = str(input("Nome do Jogador: "))
    quant = int(input(f"Quantos Jogos {historico_jogador['nome'].capitalize()} Jogou: "))
    for c in range(0, quant):
        gols_jogos.append(int(input(f" gols feito no {c}º Jogo?: ")))
    historico_jogador['gols'] = gols_jogos[:]
    historico_jogador['total_gols'] = sum(gols_jogos[:])
    registro_jogadores.append(historico_jogador.copy())
    gols_jogos.clear()
    while True:
        conti = str(input("Quer Continuar? [S/N]: ")).strip().lower()[0]
        if conti in "sn":
            break
    if conti == "n":
        break
print('_'*38)
print(f"{' Cod Nome':<20}{'gols':<13}{'total'} ")

for posicao, lista_jogador in enumerate(registro_jogadores):
    print(f"{posicao:>3} ", end='')
    for info in lista_jogador.values():
        print(f"{str(info):<15}", end='')
    print()
print("_"*38)

while True:
    escolha = int(input('Mostrar rendimento de qual jogador? [99 para parar]: '))
    if escolha == 99:
        break
    if escolha >= len(registro_jogadores):
        print("Nao existe esse jogador")
    else:
        print(f"RENDIMENTO JOGADOR {registro_jogadores[escolha]['nome']}")
        for jogo, gols in enumerate(registro_jogadores[escolha]['gols']):
            print(f'    No jogo {jogo + 1} fez {gols} gols')
    print("_"*35)

print("ENCERRADO")



