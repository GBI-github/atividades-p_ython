class Animal:
    def __init__(self, falar):
        self.falar = falar


class Gato(Animal):
    def __init__(self, falar, cor, idade):
        super().__init__(falar)
        self.cor = cor
        self.idade = idade


class Cachorro(Animal):
    def __init__(self, falar, cor, idade):
        super().__init__(falar)
        self.cor = cor
        self.idade = idade


def descrevendo_animal(Animale):
    print("um animal ruiva", Animale.falar)

    if isinstance(Animale, Gato):
        print("cor do pelo", Animale.cor)
        print("idade ", Animale.idade)


animal_aleatorio = Animal("auuu")
gato_cinza = Gato("miau miau", "cinza", 3)
cachorro_caramelo = Cachorro("au au au", "amarelo", 10)

descrevendo_animal(animal_aleatorio)
descrevendo_animal(gato_cinza)
descrevendo_animal(cachorro_caramelo)
