print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 59\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'CALCULADORA':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
maior = 0
menor = 0
while True:
    vl1 = int(input("1º Valor: "))
    vl2 = int(input("2º Valor: "))
    print("[1]- soma\n"
          "[2]- multiplicar\n"
          "[3]- maior\n"
          "[4]- menor\n"
          "[4]- novos números\n"
          "[5]- sair do programa\n")
    esc = int(input("Opção: "))
    if esc == 1:
        print(f"{vl1} + {vl2}= {vl1 + vl2}")
    if esc == 2:
        print(f"{vl1} * {vl2}= {vl1 * vl2}")
    if esc == 3:
        if vl1 > maior:
            maior = vl1
        elif maior > vl2:
            maior = vl2
        print(f"Maior numero: {maior}")
    if esc == 4:
        if vl1 > menor:
            menor = vl1
        elif menor < vl2:
            menor = vl2
        print(f"Menor numero: {menor}")
    if esc == 5:
        break
print("Programa encerrado")
