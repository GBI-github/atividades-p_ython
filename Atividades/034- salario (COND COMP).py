print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 34\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CONDIÇÃO COMPOSTA' :^32}\033[0m")
print(f"{'AUMENTO DE SALARIO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
salario = float(input("Me informe seu salario R$:  "))
print(salario)
if salario > 1250:
    aumento = (salario * 10) / 100
    print(f"Seu novo salario e de R${float(salario+ aumento)}")
if salario < 1250:
    aumento1 = (salario * 15) / 100
    print(f"Seu aumento é de R${float(salario + aumento1)}")