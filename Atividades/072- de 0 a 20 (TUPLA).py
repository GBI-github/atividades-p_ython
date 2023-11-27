from num2words import num2words
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 72 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'TUPLAS' :^32}\033[0m")
print(f"{'NOME POR EXTENSO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
numeros = "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
while True:
   numero = int(input("Informe um numero [0/20]:  "))
   if 0 <= numero <= 20:
      print(numeros[numero])
      break
   else:
      print()
      print(f"\033[31m ERROR \033[0m")
      print("tente novamente")
      print()


