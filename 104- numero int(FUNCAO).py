print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 104\033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'FUNÇÃO DEF' :^32}\033[0m")
print()
print(f"\033[32m{'NUMERO INTEIR':^32}\033[0m")
print()


def leiaint(mensagem):
    """Leia Int:
       Só aceita um número como entrada,
       o leiaint é ativada antes do print,
       não aceita strings e toda vez que alguém digitar
       algo sem ser númerico vai repetir o while,
       o return quebra o while,
       o return volta pra dentro do print assim imprimindo
       seu conteudo com o resultado númerico
        """
    while True:
        num = str(input(mensagem))
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print("\033[31mVocê não digitou um numero!\033[0m")


print("O numero digitado foi: ", leiaint('Digite um numero: '))