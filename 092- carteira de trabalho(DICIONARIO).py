print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 92 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DICIONARIO' :^32}\033[0m")
print()
print(f"\033[32m{'CTPS':^32}\033[0m")
print()
import datetime
ctps = dict()
ano_atual = datetime.date.today().year
ctps['nome'] = str(input("Nome completo: ")).strip().upper()
ctps['idade'] = int(input("Ano de nascimento: "))
ctps['ctps'] = int(input("Numero ctps, (0 não tem): "))
ctps['idade'] = ano_atual - ctps['idade']

if ctps['ctps'] != 0:
    ctps['Contratação'] = int(input("Ano de contratação: "))
    ctps['salário'] = float(input("Sálário: "))
    ap = ano_atual - ctps['Contratação']
    ap = 35 - ap
    ctps['aposentadoria'] = ctps['idade'] + ap
else:
    ctps['ctps'] = "Não tem"

print()

for k, v in ctps.items():
    print(f"{k}: {v}")




