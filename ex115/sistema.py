from Atividades.ex115.lib.arquivo import *
from time import sleep

arq = 'CursoEmVideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar novas Pessoas", "Sair do sistema"])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do sistema... Até logo!")
        sleep(2)
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m ")
    sleep(2)