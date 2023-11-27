import locale


def linha(tam=42):
    return "-" * tam


def cabecalho(nome):
    print(linha())
    print(f'{nome:^42}')
    print()


def menu(nomes):
    a = 1
    for c in nomes:
        print(f"\033[33m{a}\033[m - \033[35m{c}\033[m")
        a += 1
    op = int(input("Opção: "))
    return op


def leiacpf(msg):
    while True:
        try:
            n = int(input(msg))
            if len(str(n)) != 11:
                print("\03331m[CPF invalido!!\0330m[")
            else:
                return n
        except (ValueError, TypeError):
            print(f"\033[31mERROR!, por favor digite somente os numeros do cpf \033[0m")
            continue
        except KeyboardInterrupt:
            print("\033[31mError cpf nao especificado\033[0m")


def leiasenha():
    try:
        while True:
            senha = (input("SENHA: "))
            caractere_verificar = [".", "_", "#", ",", "@"]
            sh_val = len(' ' * 8)
            sh_inv = len(' ' * 13)
            lt_mai = any(letra.isupper() for letra in senha)
            lt_min = any(letra.islower() for letra in senha)
            num_val = any(n.isnumeric() for n in senha)
            ct_veri = any(caractere in senha for caractere in caractere_verificar)
            if lt_min and lt_mai and num_val and ct_veri and sh_val < len(senha) < sh_inv:
                return senha
            else:
                print(f"\033[31mERROR!\033[0m")
                print("\033[32mRequisitos:\n"
                      "8 caracteres.\n"
                      "Letra Maiúscula e Minúscula.\n"
                      "1 número.\n"
                      '1 desses simbolo ("." "_" "#" "," "@")\033[0m')
    except:
        print("\03331m[Error senha invalida\0330m[")


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f"\033[31mERROR!, por favor digite um número inteiro válido.\033[0m")
            continue
        except KeyboardInterrupt:
            print("\033[31mUsuário preferiu nao digitar esse numero\033[0m")
            return 0
        else:
            return n


def converter_em_num(v):
    valor_sem_simbolos = v.replace('R$', '').replace('.', '').replace(',', '.')
    return float(valor_sem_simbolos)


def conversor(msg):
    while True:
        try:
            n = msg
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            valor_formatado = locale.currency(n, grouping=True)
        except (ValueError, TypeError):
            print(f"\033[31mERROR!, por favor informe o Deposito.\033[0m")
        except KeyboardInterrupt:
            print("\033[31mUsuário preferiu nao digitar esse numero\033[0m")
            return 0
        else:
            return valor_formatado