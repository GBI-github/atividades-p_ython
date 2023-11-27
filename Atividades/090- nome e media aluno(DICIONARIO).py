print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 90 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DICIONARIO' :^32}\033[0m")
print()
print(f"\033[32m{'APROVADO/REPROVADO':^29}\033[0m")

dados_aluno = dict()
dados_gerais = list()
while True:
    dados_aluno['nome'] = str(input("Nome Aluno: "))
    dados_aluno['nota'] = float(input(f"Média  de {dados_aluno['nome']}: "))
    if dados_aluno["nota"] < 7:
        dados_aluno['estado do aluno'] = 'reprovado'
    if dados_aluno['nota'] >= 7:
        dados_aluno['estado do aluno'] = 'aprovado'
    dados_gerais.append(dados_aluno.copy())
    break
print()
for dados in dados_gerais:
    for k, v in dados.items():
        print(f"{k}: {v}")
