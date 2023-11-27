print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 29\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CONDIÇÃO COMPOSTA' :^32}\033[0m")
print(f"{'LIMITE DE VELOCIDADE':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
velocidade = int(input("Velocidade do seu carro Km: "))
if velocidade < 80:
    print("Pode ir")
else:
    multa = float(velocidade - 80) * 7.00
    print("Limite de 80Km atingido!!!")
    print(f"sua multa é de {multa}R$ ")
