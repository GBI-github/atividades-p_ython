print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 032\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DUPLA LISTA' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
dados_pessoais = []
esc = 1
while esc != "0":
    print("Registro de dados: ")
    print(f"{'-' * 32}")
    nome = str(input("Informe seu nome completo: "))
    idade = str(input("Informe sua idade: "))
    sexo = str(input("Informe seu sexo: "))
    estado_civil = str(input("Informe seu estado civil: "))
    dados_individuais = [nome, idade, sexo, estado_civil]
    dados_pessoais.append(dados_individuais[:])
    esc = str(input("Quer Parar? Digite- 0: "))
    print()
    print(f"\033[32m{'REGISTRO REALIZADO COM SUCESSO' :^32}\033[0m")
    print(f"{'-' * 32}")
    print()
lista = ["nome: ", "idade: ", "sexo: ", "estado_civil: "]
for c in range(0, len(dados_pessoais)):
    print(f"\033[32m{f'{c + 1}º REGISTRO:':^32}\033[0m")
    print()
    for c1 in range(0, len(dados_pessoais[c])):
        print(lista[c1], end='')
        print(dados_pessoais[c][c1])
    print(f"{'-' * 32}")

# 1º fiz uma lista pra guardar as informações do usuário, criei outra pra guardar essas informações de forma
# aninhada, depois criei o 2° "for" pra mostra-las na tela do usuário, o 1º "for" busca todas as posições na lista
# que tem as informações dos usuários aninhadas. Após esse procedimento o 2º "for" Age dentro do primeiro "for" e
# busca as informações individuais que a nele, O resto foi somente modificação de visualização pra deixar o usuário
# mais confortável
