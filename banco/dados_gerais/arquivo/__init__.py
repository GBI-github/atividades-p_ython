from banco.dados_gerais.interfase import *
import time


def existearquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False

    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("\03331m[Ouve um erro na criação da conta\0330m[")
    else:
        print(f"\03332m[Usuário cadastrado com sucesso!\0330m[")


def cpfexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cpfexistente(nome, senha, usuario):
    try:
        a = open(nome, 'at')
    except:
        print("\03331m[ERRO na abertura da conta\0330m[")
    else:
        try:
            a.write(f"{usuario};{senha};{0}")
        except:
            print("\03331m[ERRO, ao escrever os dados\0330m[")
        else:
            a.close()


def saldo(msg):
    with open(msg, 'r') as arquivo:
        dados = arquivo.read()
    numeros = dados.split(';')
    ultimo_numero = numeros[-1]
    return ultimo_numero


def senhaexistente(msg, senha):
    try:
        a = open(msg, "rt")
    except:
        print("Error")
    else:
        for l in a:
            dado = l.split(';')
            if senha == dado[1]:
                print(linha())
                print(f"{'CONTA BANCARIA':^42}")
                print()
                print("NOME:",dado[0])
                print()
                print(f"Saldo: {saldo(msg)}")

                print()
                time.sleep(2)
                print(linha())
                while True:
                    resposta = menu(["Sacar", "Depositar", "Sair"])
                    if resposta == 1:
                        valor = converter_em_num(str(saldo(msg)))
                        if valor == 0:
                            print("\03331m[SALDO INSUFICIENTE\0330m[ ")
                            continue

                        saque = leiafloat("valor do Saque: R$ ")
                        print("Aguarde completar a transação...")
                        time.sleep(2)
                        print()
                        if saque > valor:
                            print("\03331m[SALDO INSUFICIENTE\0330m[ ")
                            continue

                        if saque < valor:
                            valor1 = converter_em_num(saldo(msg))
                            valor_sub = valor1 - saque
                            valor_sub = conversor(valor_sub)
                            try:
                                a = open(msg, 'at')
                            except:
                                print("\03331m[ERRO na abertura da conta\0330m[")
                            else:
                                try:
                                    a.write(f";{valor_sub}")
                                except:
                                    print("\03331m[ERRO, ao fazer Saque\0330m[")
                                else:
                                    a.close()
                                    print("Saldo: ", saldo(msg))

                                    print(linha())
                                    return False
                    if resposta == 2:
                        deposito = leiafloat("Valor do Deposito: R$ ")
                        print("Aguarde o deposito...")
                        time.sleep(2)
                        valor1 = converter_em_num(saldo(msg))
                        valor_total = valor1 + deposito
                        valor_total = conversor(valor_total)
                        try:
                            a = open(msg, 'at')
                        except:
                            print("\03331m[ERRO na abertura da conta\0330m[")
                        else:
                            try:
                                a.write(f";{valor_total}")
                            except:
                                print("\03331m[ERRO, ao fazer Deposito\0330m[")
                            else:
                                a.close()
                                print()
                                print("Saldo: ", saldo(msg))
                                print(linha())
                                return False
                    if resposta >= 3:
                        break
