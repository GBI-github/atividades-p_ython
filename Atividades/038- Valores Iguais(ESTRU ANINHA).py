print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 38\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA ANINHADA' :^32}\033[0m")
print(f"{'BASE DE VALORES':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
num1 = int(input("1º Numero: "))
num2 = int(input("2º Numero: "))
if num1 > num2:
    print("O 1º valor é maior")
elif num2 > num1:
    print("o 2º valor é maior")
elif num2 == num1:
    print("Valores iguais ")