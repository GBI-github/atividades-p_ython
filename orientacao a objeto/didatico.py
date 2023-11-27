class Clientes:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("plano invalido")

    def mudar_plano(self,  novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano invailido")

    def ver_filme(self, filme, planno_filme):
        if self.plano == planno_filme:
            print(f"Ver filme {filme}")
        elif self.plano == "premium":
            print(f"Ver filme {filme}")
        elif self.plano == "basic" and planno_filme == "premium":
            print("Acesso negado, Atualize o plano")
        else:
            print("plano invalido")


cliente = Clientes(nome="gabriel", email="jgga07000@gmail.com", plano="basic")
print(cliente.plano)
cliente.ver_filme("Harry Poter", "premium")

cliente.mudar_plano("premium")
print(cliente.plano)
cliente.ver_filme("Harry Poter", "premium")
