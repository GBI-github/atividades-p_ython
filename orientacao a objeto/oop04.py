class Calculadora:
    def __init__(self, menu, somar):
        self.menu = menu
        self.somar = somar

    def exibir_menu(self):
        a = 1
        for c in self.menu:
            print(f"\033[33m{a}\033[m - \033[35m{c}\033[m")
            a += 1
        op = int(input("Opção: "))
        return op

    def somar_numero(self):
        numeros = list(map(int, input("Digite os números separados por espaço: ").split()))
        return sum(numeros)


calculadora = Calculadora(["Somar", "Multiplicar", "Subtrair", "Dividir"], '')
opcao = calculadora.exibir_menu()

if opcao == 1:
    soma_total = calculadora.somar_numero()
    print(f"A soma dos números é: {soma_total}")
