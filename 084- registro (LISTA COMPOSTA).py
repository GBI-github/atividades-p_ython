print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 84 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA COMPOSTA-DUPLA LISTA' :^32}\033[0m")

print(f"\033[4;37m{'-' * 32}\033[0m")
registro_temporario = []
registro_principal = []
pesado = leve = 0
import time
while True:
    registro_temporario.append(str(input("Nome: ")))
    registro_temporario.append(int(input("Peso: ")))
    if len(registro_principal) == 0:
        pesado = leve = registro_temporario[1]
    elif registro_temporario[1] > pesado:
        pesado = registro_temporario[1]
    if registro_temporario[1] < leve:
        leve = registro_temporario[1]
    registro_principal.append(registro_temporario[:])
    registro_temporario.clear()
    escolha = str(input("Quer continuar[S/N]: ")).lower().strip()[0]
    if escolha == "n":
        print("FINALIZANDO...")
        time.sleep(1)
        print()
        print()
        print(f"\033[31m{'REGISTRO FINALIZADO':^32}\033[0m")
        print(f"\033[4;37m{'-' * 32}\033[0m")
        break
    print("REGISTRANDO...")
    time.sleep(1)
    print()
    print(f"\033[32m{'REGISTRO REALIZADO COM SUCESSO':^32}\033[0m")
    print()
    print(f"\033[4;37m{'-' * 32}\033[0m")

print("-=" * 30)
print(f"total de dados cadastrado {len(registro_principal)}")
print(f"Maior peso: {pesado}Kg."
      f"\nReferente a ", end='')
for c in registro_principal:
    if c[1] == pesado:
        print(c[0], end=' ')
print("")
print(f"Menor peso: {leve}Kg."
      f"\nReferente a ", end='')
for c in registro_principal:
    if c[1] == leve:
        print(c[0], end=' ')
print()