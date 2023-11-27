print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 39\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA ANINHADA' :^32}\033[0m")
print(f"{'ANO DE NASCIMENTO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
ano = int(input("Seu ano de nascimento: "))
idade = 2023 - ano
if idade < 18:
    print(f"Ainda falta {18- idade} pra você se alistar")
elif idade == 18:
    print(f"você vai servir esse ano")
else:
    print(f"Você passou {idade- 18} anos da data de alistamento")
