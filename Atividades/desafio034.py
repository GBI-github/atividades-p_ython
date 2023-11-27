print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 034\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DUPLA LISTA' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
memoria = []
dados_temporarios = []
while True:
    dados_temporarios.append(str(input("Nome: ")))
    dados_temporarios.append(int(input("Idade: ")))
    memoria.append(dados_temporarios[:])
    dados_temporarios.clear()
    esc = str(input("Continuar? [S/N]: ")).strip().lower()[0]
    if esc == "n":
        break
print(f"Pessoas cadastradas: {len(memoria)}")

soma = 0
acima_media = []
for c in range(len(memoria)):
    soma = (soma + memoria[c][1])/len(memoria)

for c in range(len(memoria)):
    if memoria[c][1] > soma:
        acima_media.append(memoria[c][0])
        acima_media.append(memoria[c][1])

print(f"Media de idade: {soma:.2f}")

print(f"Pessoas acima da media ", acima_media)
