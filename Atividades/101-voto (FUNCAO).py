print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 101 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'FUNÇÃO DEF' :^32}\033[0m")
print()
print(f"\033[32m{'VOTO':^32}\033[0m")
print()


def voto(nascimento):
    import datetime
    ano = datetime.datetime.now().year
    idade = ano - nascimento
    if 18 <= idade <= 68:
        print(f"Idade: {idade} Anos")
        print("Voto: \033[32mObrigatório\033[0m")
    if idade < 18:
        print(f"Idade: {idade} Anos")
        print("Voto: \033[31mNÃO\033[0m Vota")
    else:
        print(f"Idade: {idade} Anos")
        print("Voto: \033[32mOpcional\033[0m")


print(f"\033[4;37m{'-' * 32}\033[0m")
ano_nasc = int(input("Ano de Nascimento: "))
voto(ano_nasc)