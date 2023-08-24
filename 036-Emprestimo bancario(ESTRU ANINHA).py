print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 36\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA ANINHADA' :^32}\033[0m")
print(f"{'EMPRÉSTIMO PRA CASA':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
emprestimo = float(input("valor da casa: "))
salario = float(input("Seu salario: "))
ano = int(input("Quantos anos deseja pagar: "))
porcentagem = (salario * 30) / 100
mes_pagar = emprestimo / (ano * 12)
if mes_pagar > porcentagem:
    print("Empréstimo Negado")
    print("Infelizmente voce não pode financiar essa casa")
elif mes_pagar <= porcentagem:
    print("Empréstimo Aprovado")
