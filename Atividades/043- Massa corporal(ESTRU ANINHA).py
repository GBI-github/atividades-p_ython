print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 43\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA ANINHADA' :^32}\033[0m")
print(f"{'IMC':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Abaixo do peso")
    print(f"Imc: {imc}")
elif 18.5 <= imc < 25:
    print("Peso ideal")
    print(f"Imc: {imc:.2f}")
elif 25 <= imc < 30:
    print("Sobrepeso")
    print(f"Imc: {imc:.2f}")
elif 30 <= imc < 40:
    print("Obesidade")
    print(f"Imc: {imc:.2f}")
elif imc > 40:
    print("Obesidade mórbida")
    print(f"Imc: {imc:.2f}")