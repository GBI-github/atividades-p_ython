def dados(p):
    while True:
        if p.isnumeric():
            p = float(p)
            return p
        print(f"\033[31mNumero '{p}' é invalido\033[0m")
        p = input("Digite o preço: R$")
