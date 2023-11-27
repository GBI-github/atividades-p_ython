class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura): #atributos
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    @staticmethod
    def passar_canal(botao):
        if botao == "+":
            print("Aumentar o Canal")
        if botao == '-':
            print("Diminuir o Canal")


controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
print(controle_remoto.cor)
controle_remoto.passar_canal('+')

controle_remoto2 = ControleRemoto("cinza", "10cm", "2cm", "2cm")
print(controle_remoto2.largura)
controle_remoto2.passar_canal('-')