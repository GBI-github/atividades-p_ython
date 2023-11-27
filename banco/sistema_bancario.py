from banco.dados_gerais.arquivo import *
while True:
    cabecalho('BANCO TAI')
    resp = menu(["Cadastrar", "Entrar", "Sair"])
    if resp == 1:
        try:
            while True:
                cabecalho("NOVO CADASTRO")
                nome = str(input("NOME: ")).upper().strip()
                cpf = leiacpf("CPF: ")
                senha = leiasenha()
                arq = str(cpf).replace(" ", '')
                if not existearquivo(arq):
                    criararquivo(arq)
                    cpfexistente(arq, senha, nome)
                    print()
                    break
                else:
                    print()
                    print(f"\03331m[a Conta com o cpf {cpf} ja é existente\0330m[ ")
                    print()
        except:
            break
    if resp == 2:
        try:
            while resp == 2:
                cabecalho("usuário")
                print()
                print()
                cpf = leiacpf('CPF: ')
                ap = str(cpf)
                if cpfexiste(ap):
                    if senhaexistente(ap, leiasenha()):
                        break
                else:
                    print()
                    print("\03331m[CONTA INEXISTENTE!!\0330m[")
                    break
                resp = 0
        except:
            break
        else:
            print(f"{'Obrigado por acessar nosso banco':^42}")
            continue
    if resp == 3:
        break
    else:
        break
