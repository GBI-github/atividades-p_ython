print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 13\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'PORCENTAGEM' :^32}\033[0m")
print(f"{'15% DE AUMENTO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
salarioantigo = float(input("Qual é o seu salario atual?: R$"))
salarionovo = (15 * salarioantigo) / 100
print(f"Seu novo salario e de R${salarionovo + salarioantigo:.2f}")
