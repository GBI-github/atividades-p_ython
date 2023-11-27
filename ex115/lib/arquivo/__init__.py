from Atividades.ex115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')  # é por causa do + que o arquivo é criado
        a.close()
    except:
        print("Ouve um erro na criação do arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao abrir arquivo")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        print(f"{'NOME':<30}{'IDADE'}")
        print()
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0].capitalize():<30}{dado[1]} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("ERRO na abertura do arquivo")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("ERRO, ao escrever os dados")
        else:
            print(f"Novo registro de {nome} adicionado")
            a.close()
