print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 81 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'LISTA' :^32}\033[0m")
print(f"{'INFORMAÇÃO LISTA':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[0;31m Fechar o programa DIGITE- 0\033[0m")
lista = []
c = 0
while True:
    c += 1
    num = int(input(f"{c}º Valor:"))
    if num != 0:
        lista.append(num)
    if num == 0:
        break
        print("\033[31mPrograma finalizado\033[0m")
if len(lista) > 1:
    print(f"{len(lista)} números digitados ")
else:
    print(f"{len(lista)} número digitado ")
lista1 = lista[:]
lista1.sort(reverse=True)
print(f"Ordem decrescente{lista1}")
if lista.count(5) != 0:
    print(f"O numero 5 apareceu {lista.count(5)} vezes")

