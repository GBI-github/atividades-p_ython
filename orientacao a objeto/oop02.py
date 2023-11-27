import math


class Calculadora:
    def __init__(self, menu):
        self.menu = menu

    def exibir_menu(self):
        a = 1
        for c in self.menu:
            print(f"\033[33m{a}\033[m - \033[35m{c}\033[m")
            a += 1
        op = int(input("Opção: "))
        return op

    def somar_numero(self):
        c = 1
        soma_numeros = list()
        while True:
            soma_numeros.append(int(input(f"{c}º Valor: ")))
            c += 1
            if c > 2:
                resp = str(input("Continuar?[S/N]: ")).upper().strip()[0]
                if resp != "S":
                    break
                continue
        print(f"A soma total dos valores {soma_numeros} é: ", end='')
        return sum(soma_numeros)

    def multiplicar_valor(self):
        c = 1
        multiplica_numeros = list()
        while True:
            multiplica_numeros.append(int(input(f'{c}ºValor: ')))
            c += 1
            if c > 2:
                resp = str(input("Continuar?[S/N]: ")).upper().strip()[0]
                if resp != "S":
                    break
                continue
        print(f"A multiplicação total dos valores {multiplica_numeros} é: ", end='')
        return math.prod(multiplica_numeros)

    def subtrair_numeros(self):
        c = 1
        subtrair_numeros = list()
        while True:
            subtrair_numeros.append(int(input(f'{c}ºValor: ')))
            c += 1
            if c > 2:
                resp = str(input("Continuar?[S/N]: ")).upper().strip()[0]
                if resp != "S":
                    break
                continue
        print(f"A subtração total dos valores {subtrair_numeros} é: ", end='')
        resultado = subtrair_numeros[0]
        for elemento in subtrair_numeros[1:]:
            resultado = resultado - elemento
        return resultado

    def dividir_numeros(self):
        c = 1
        dividir_numeros = list()
        while True:
            dividir_numeros.append(int(input(f'{c}ºValor: ')))
            c += 1
            if c > 2:
                resp = str(input("Continuar?[S/N]: ")).upper().strip()[0]
                if resp != "S":
                    break
                continue
        print(f"A multiplicação total dos valores {dividir_numeros} é: ", end='')
        resultado = dividir_numeros[0]
        for elemento in dividir_numeros[1:]:
            resultado = resultado / elemento
        return resultado


calculadora = Calculadora(["Somar", "Multiplicar", "Subtrair", "Dividir"])
opcao = calculadora.exibir_menu()
if opcao == 1:
    soma_total = calculadora.somar_numero()
    print(soma_total)
if opcao == 2:
    multiplicar = calculadora.multiplicar_valor()
    print(multiplicar)
if opcao == 3:
    subtrair = calculadora.subtrair_numeros()
    print(subtrair)
if opcao == 4:
    dividir = calculadora.dividir_numeros()
    print(dividir)
