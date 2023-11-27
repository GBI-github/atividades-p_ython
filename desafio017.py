import random
import time
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 017\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{' DE 1 A 100' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")

chance = str(input("Vamos rodar o dado? [S/N]: ")).strip().lower()
if chance[0] == "s":
    while True:

        dado = random.randint(0, 6)
        print("Rolando dado...")
        time.sleep(3)
        print()
        print("resultado:", dado)
        continua = int(input("\n---------------------"
                             "\n|[1]- pra parar!    |"
                             "\n|[2]- pra continuar |"
                             "\n---------------------"
                             "\nOpção: "))
        if continua == 1:
            break
else:
    print("Fim do programa!")
print("Fim do programa!")