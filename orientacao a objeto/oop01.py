class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def apresentar(self):
        return f"Nome: {self.nome} tem {self.idade} e mora na Cidade de {self.cidade}"


name = input("Nome: ").capitalize()
year = int(input("Idade: "))
city = input("Cidade: ").capitalize()

identidade = Pessoa(name, year, city)

print(identidade.apresentar())