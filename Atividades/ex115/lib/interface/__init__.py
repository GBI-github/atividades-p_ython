def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f"\033[31mERROR!, por favor digite um número inteiro válido.\033[0m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu nao digitar esse numero\033[0m")
            return 0
        else:
            return n


def linha(tam=42):  # p1
    return "-" * tam


def cabecalho(txt):  # p2
    print(linha())
    print(f"{txt:^42}")
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for it in lista:
        print(f"\033[33m{c}\033[m - \033[35m{it}\033[m")
        c += 1
    print(linha())
    opc = leiaint("\033[33mSua Opção:\033[m ")
    return opc
