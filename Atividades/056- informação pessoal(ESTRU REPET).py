print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 56\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'INFORMAÇÕES PESSOAIS':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
totmaior = 0
maioridade = 0
maiornome = ''
mediaidade = 0
for contador in range(1, 4):
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    genero = str(input("Sexo[F/M]: ")).lower().strip()
    if genero == "feminino" or "f" or "feminina":
        if idade < 20:
            totmaior = totmaior + 1
    if genero == "maculino" or "m" or "masculina":
        if idade > maioridade:
            maioridade = idade
            maiornome = nome
    mediaidade = idade + mediaidade
print(f"A media de idade e {mediaidade/3}")
print(f"O homem mais velho é: {maiornome}\n {maioridade} Anos")
if totmaior < 2:
    print(f"tem {totmaior} mulher menor de 20 anos")
else:
    print(f"tem {totmaior} mulheres menores de 20 anos")

