import locale


def linha(tamanho=42):
    return "-" * tamanho


def cabecalho(mensagem):
    print(linha())
    print(f"{mensagem:^42}")
    print()


def leiaint(msg):
    while True:
        try:
            a = int(input(msg))
        except(ValueError, TypeError):
            print("\033[31mERROR opção invalida!!\033[0m")
        except KeyboardInterrupt:
            print("\033[31mOpção não informada!")
        else:
            return a


def leiafloat(msg):
    while True:
        try:
            a = float(input(msg))
        except ValueError:
            print("\033[31mERROR não , e sim .!!\033[0m")
        except TypeError:
            print("\033[31mERROR informe o Preço\033[0m")
        except KeyboardInterrupt:
            print("\033[31mPreço não informado!")
        else:
            return a


def menu(opcoes):
    a = 1
    for c in opcoes:
        print(f"{a}-{c}")
        a += 1
    print()
    op = leiaint("Opção: ")
    return op


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


def converter_em_num(v):
    valor_sem_simbolos = v.replace('R$', '').replace('.', '').replace(',', '.')
    return float(valor_sem_simbolos)

