import time
import math
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 71 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'CAIXA ELETRÔNICO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
valor = []
valor_total = 0
while True:
    # aqui mostra as opcões do caixa
    print()
    print("-=" * 15)
    print("Bem-vindo ao Caixa Eletrônico!")
    print("-=" * 15)
    print("Selecione uma opção:")
    print("1. Saldo")
    print("2. Saque")
    print("3. Depósito")
    print("4. Sair")
    print("-=" * 15)
    op = int(input("Opção: "))

    match op:
        case 1:
            # aqui abre a interface de saldo do usuario
            print("-=" * 15)
            print("Saldo Disponível:")
            print(f"R$ {valor_total}")
            print("Deseja realizar outra operação?")
            print("1. Sim")
            print("2. Não")
            op1 = int(input("Opção: "))
            print("-=" * 15)
            print()

            match op1:
                case 1:
                    # aqui pergunta qual opção o usuario quer abrir
                    print("1.Deposito")
                    print("2.Saque")
                    print("2.Lobby")
                    print()
                    op2 = int(input("Opção: "))
                    print("-=" * 15)
                    match op2:
                        case 1:
                            # aqui vai mostrar ao usuario e perguntar quanto ele quer depositar
                            print("Depósito")
                            print()
                            deposito = float(input("Valor: R$ "))
                            print("-=" * 15)
                            print()
                            print("Confirmar:\n"
                                  "[1] Sim\n"
                                  "[2] Não\n")
                            print("-=" * 15)
                            op3 = int(input("Opção: "))
                            match op3:
                                case 1:
                                    # aqui soma o valor depositado e sobe o valor pra dentro da lista "valor"
                                    valor_total += deposito
                                    valor.append(valor_total)
                        case 2:
                            # aqui vai perguntar ao usuario quanto ele quer sacar
                            print("Saldo Disponível:R$", valor_total)
                            print("Valor do Saque")
                            saque = float(input("Valor: R$ "))

                            if saque > valor_total:
                                print()
                                print(f"\033[31m Saldo Indisponível\033[0m")

                            if saque < valor_total:
                                valor_total += -saque
                                print("-=" * 15)
                                print()
                                print("Confirmar:\n"
                                      "[1] Sim\n"
                                      "[2] Não\n")
                                op4 = int(input("Opção: "))
                                print("Saque realizado com sucesso.")
                                print("-=" * 15)

                                if op4 == 1:
                                    # aqui vai mostrar a quantidade de cedula sacada
                                    print("sacando...")
                                    time.sleep(4)
                                    print()
                                    cedulas_100 = saque // 100
                                    saque %= 100

                                    cedulas_50 = saque // 50
                                    saque %= 50
                                    cedulas_20 = saque // 20
                                    saque %= 20
                                    cedulas_10 = saque // 10
                                    saque %= 10
                                    cedulas_5 = saque // 5
                                    saque %= 5
                                    cedulas_1 = saque // 1
                                    saque %= 1
                                    print(f"\033[4;37m{'-' * 32}\033[0m")
                                    print(f"\033[32m{'SALDO' :^32}\033[0m")
                                    print("Saldo atual: R$", valor_total)
                                    print("Cédulas:")

                                    if cedulas_100 > 0:
                                        if cedulas_100 == 1:
                                            print(f" {math.ceil(cedulas_100)} Cédula de R$100: ")
                                        elif cedulas_100 > 1:
                                            print(f" {math.ceil(cedulas_100)} Cédulas de R$100: ")

                                    if cedulas_50 > 0:
                                        if cedulas_50 == 1:
                                            print(f" {math.ceil(cedulas_50)} Cédula de R$50: ")
                                        elif cedulas_50 > 1:
                                            print(f" {math.ceil(cedulas_50)} Cédulas de R$50: ")

                                    if cedulas_20 > 0:
                                        if cedulas_20 == 1:
                                            print(f" {math.ceil(cedulas_20)} Cédula de R$20: ")
                                        elif cedulas_20 > 1:
                                            print(f" {math.ceil(cedulas_20)} Cédulas de R$20: ")

                                    if cedulas_10 > 0:
                                        if cedulas_10 == 1:
                                            print(f" {math.ceil(cedulas_10)} Cédula de R$10: ")
                                        elif cedulas_10 > 1:
                                            print(f" {math.ceil(cedulas_10)} Cédulas de R$10: ")

                                    if cedulas_5 > 0:
                                        if cedulas_5 == 1:
                                            print(f" {math.ceil(cedulas_5)} Cédula de R$5: ")
                                        elif cedulas_5 > 1:
                                            print(f" {math.ceil(cedulas_5)} Cédulas de R$5: ")

                                    if cedulas_1 > 0:
                                        if cedulas_1 == 1:
                                            print(f" {math.ceil(cedulas_5)} Moeda de R$1: ")
                                        elif cedulas_1 > 1:
                                            print(f" {math.ceil(cedulas_5)} Moedas de R$1: ")

                                    print()
                                    print(f"\033[4;37m{'-' * 32}\033[0m")
        case 2:
            print("-=" * 15)
            print("Saldo Disponível:")
            print(f"R$ {valor_total}")
            print("Valor do Saque")
            saque = float(input("Valor: R$ "))

            if saque > valor_total:
                print()
                print(f"\033[31m Saldo Indisponível\033[0m")


            if saque < valor_total:
                valor_total += -saque
                print("-=" * 15)
                print()
                print("Confirmar:\n"
                      "[1] Sim\n"
                      "[2] Não\n")
                op4 = int(input("Opção: "))
                print("Saque realizado com sucesso.")
                print("-=" * 15)

                if op4 == 1:
                    # aqui vai mostrar a quantidade de cedula sacada
                    print("sacando...")
                    time.sleep(4)
                    print()
                    cedulas_100 = saque // 100
                    saque %= 100

                    cedulas_50 = saque // 50
                    saque %= 50
                    cedulas_20 = saque // 20
                    saque %= 20
                    cedulas_10 = saque // 10
                    saque %= 10
                    cedulas_5 = saque // 5
                    saque %= 5
                    cedulas_1 = saque // 1
                    saque %= 1
                    print(f"\033[4;37m{'-' * 32}\033[0m")
                    print(f"\033[32m{'SALDO' :^32}\033[0m")
                    print("Saldo atual: R$", valor_total)
                    print("Cédulas:")

                    if cedulas_100 > 0:
                        if cedulas_100 == 1:
                            print(f" {math.ceil(cedulas_100)} Cédula de R$100: ")
                        elif cedulas_100 > 1:
                            print(f" {math.ceil(cedulas_100)} Cédulas de R$100: ")

                    if cedulas_50 > 0:
                        if cedulas_50 == 1:
                            print(f" {math.ceil(cedulas_50)} Cédula de R$50: ")
                        elif cedulas_50 > 1:
                            print(f" {math.ceil(cedulas_50)} Cédulas de R$50: ")

                    if cedulas_20 > 0:
                        if cedulas_20 == 1:
                            print(f" {math.ceil(cedulas_20)} Cédula de R$20: ")
                        elif cedulas_20 > 1:
                            print(f" {math.ceil(cedulas_20)} Cédulas de R$20: ")

                    if cedulas_10 > 0:
                        if cedulas_10 == 1:
                            print(f" {math.ceil(cedulas_10)} Cédula de R$10: ")
                        elif cedulas_10 > 1:
                            print(f" {math.ceil(cedulas_10)} Cédulas de R$10: ")

                    if cedulas_5 > 0:
                        if cedulas_5 == 1:
                            print(f" {math.ceil(cedulas_5)} Cédula de R$5: ")
                        elif cedulas_5 > 1:
                            print(f" {math.ceil(cedulas_5)} Cédulas de R$5: ")

                    if cedulas_1 > 0:
                        if cedulas_1 == 1:
                            print(f" {math.ceil(cedulas_5)} Moeda de R$1: ")
                        elif cedulas_1 > 1:
                            print(f" {math.ceil(cedulas_5)} Moedas de R$1: ")

                    print()
                    print(f"\033[4;37m{'-' * 32}\033[0m")
        case 3:
            print("-=" * 15)
            print("Saldo Disponível:")
            print(f"R$ {valor_total}")
            print("Depósito")
            print()
            deposito = float(input("Valor: R$ "))
            print("-=" * 15)
            print()
            print("Confirmar:\n"
                  "[1] Sim\n"
                  "[2] Não\n")
            print("-=" * 15)
            op3 = int(input("Opção: "))
            match op3:
                case 1:
                    # aqui soma o valor depositado e sobe o valor pra dentro da lista "valor"
                    valor_total += deposito
                    valor.append(valor_total)
        case 4:
            break
print()
print(f"\033[31mAÇÃO FINALIZADA\033[0m")
print(f"\033[32m{'SALDO: R$'}{valor_total}\033[0m")

