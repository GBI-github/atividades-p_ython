class Caneca:
    formato = "Cilindrico com alça lateral"

    def __init__(self,nome,logo,cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'cheia'

    def Beber(self):
        self.status = "Vazia"

    def Encher(self):
        self.status = "cheia"


class CanecaLondrina(Caneca):
    def __init__(self, nome, logo, cor):
        super().__init__(nome, logo, cor)
        self.nome = "queijo"


caneca1 = Caneca('caneca londrina', 'cidade de londres', 'branca')
caneca2 = Caneca('caneca byleaner', "foguetao", "branca")
print("a caneca", caneca1.nome,"possui a logo", caneca1.logo)
print("a caneca", caneca2.nome,"possui a logo", caneca2.logo)
caneca1.Beber()
caneca1.Encher()

caneca2.Beber()
print("caneca1: ",caneca1.status)
print("caneca2: ",caneca2.status)