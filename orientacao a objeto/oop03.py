class usuario:
    def __init__(self, nome):
        self.nome = nome

    def bem_vindo(self):
        n = self.nome
        return n


namy = str(input("Nome: "))
user = usuario(namy)
print("Seja bem vindo", user.bem_vindo())
