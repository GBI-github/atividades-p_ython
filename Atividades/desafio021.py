print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 021\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'Numeros' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
while True:
    num = int(input("Informe um numero: "))
    print(f"\n\033[4m{'-' * num*4}\033[0m\n")
    for n in range(1, num+1):
        print(f"\033[31m{n:^2}..\033[0m", end="")
    print(f"\n\033[4;37m{'-' * num*4}\033[0m\n")

    print("\nNumeros divisiveis por 3: ")
    print()
    for n in range(1, num):
        if n % 3 == 0:
            print(f"{n}..", end="")
    print()
    escolha = str(input("\nQuer continuar [S/N]: ")).lower().strip()
    if escolha[0] == "n":
        break

