print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 37\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA ANINHADA' :^32}\033[0m")
print(f"{'BASE DE CONVERSÃO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
numero = int(input("Informe um numero: "))
print(f"{'CONVERSOR':^32}")
print()
print("[1]- Numero binario\n"
      "[2]- Numero octal\n"
      "[3]- Numero hexadecimal\n")
escolha = int(input("Opção: "))
if escolha == 1:
    print(f"numero binario:\n {bin(numero)}")
elif escolha == 2:
    print(f"Numero octal:\n {oct(numero)}")
elif escolha == 3:
    print(f"Numero hexadecimal:\n {hex(numero)}")
else:
    print("Escolha uma das opções")
