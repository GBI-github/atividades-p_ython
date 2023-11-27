def leiaint():
    while True:
        try:
            num = int(input("Informe um numero inteiro: "))
            return num
        except (ValueError, TypeError):
            print(f"\033[31mERROR!, por favor digite um número inteiro válido.\033[0m")
            continue
        except KeyboardInterrupt:
            print("\033[31mUsuário preferiu nao digitar esse numero\033[0m")
            num = "inexistente"
            return num


def leiafloat():
    while True:
        try:
            num = float(input("Informe um numero Real: "))
            return num
        except (ValueError, TypeError):
            print(f"\033[31mERROR!, por favor digite um número Real válido.\033[0m")
            continue
        except KeyboardInterrupt:
            print("\033[31mUsuário preferiu nao digitar esse numero\033[0m")
            num = "inexistente"
            return num
    num = int(input("Digite um numero Real: "))




