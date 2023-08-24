print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 63\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'SEQUENCIA DE FIBONACCI':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
verdadeiro = True
while verdadeiro:
    numero = int(input("Numero de termo que voce quer usar: "))
    n_terms = numero
    fib_seq = [0, 1]
    while len(fib_seq) < n_terms:
        next_number = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_number)
    print(fib_seq)
    desicao = str(input("Quer continuar? [S/N]: ")).lower().strip()
    if desicao == desicao[0]:
        verdadeiro = False

