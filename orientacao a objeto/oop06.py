class livro:
    def __init__(self, folha, estilo, autor, nome):
        self.folha = folha
        self.estilo = estilo
        self.autor = autor
        self.nome = nome


class livrofic(livro):
    def __init__(self, folha, estilo, autor, nome):
        super().__init__(folha, estilo, autor, nome)


liv = livro(750, 'romance', "sid-morty", "por ventura")
liv2 = livrofic(550, "ficção", "megan", "all fox")

print(f"O livro de {liv.estilo}, do autor {liv.autor}\n", "nomeado como", f'"{liv.nome}"\n', f"contem {liv.folha} ")
print(f"paginas, e cada uma\n prende a atenção e a curiosidade dos leitores ")
print()
print(f"enquanto o livro de {liv2.estilo} do autor {liv2.autor} chamado {liv2.nome}, impacta a todos pela sua fantasia")
