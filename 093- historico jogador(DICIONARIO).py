print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 93 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DICIONARIO' :^32}\033[0m")
print()
print(f"\033[32m{'HISTORICO DE PARTIDAS':^32}\033[0m")
print()
historico_jogador = dict()
historico_jogador['nome'] = str(input("Nome do jogador: "))
quant = int(input("Quantos jogos jogou: "))
gols_feitos = list()
soma = 0
print()
soma1 = 0
for c in range(1, quant + 1):
    quantidade = int(input(f"gols feito no {c}º Jogo?: "))
    gols_feitos.append(quantidade)
    soma += quantidade
historico_jogador["gols"] = gols_feitos[:]
historico_jogador['total_gols'] = soma

print()
print(f"o Jogador {historico_jogador['nome']} jogou {quant} partidas.")
soma2 = 0
for v in historico_jogador['gols']:
    soma2 += 1
    print(f"    => Na {soma2}º partida, fez {v} gols")
print()
print(f" {historico_jogador['total_gols']} Gols.")
