import random
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 010\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CRIPTOGRAFANDO' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"{'criptografar mensagem' :^32}")
frase = input("digite uma frase: ").strip()
frase = frase.replace(" ", "")
troca = ''
for letra in frase:
    if letra.isalpha():
        numero_aleatorio = random.randint(0, 1)
        troca = troca + str(numero_aleatorio)
print("criptografando")
print(troca)




