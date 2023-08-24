print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 40\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA ANINHADA' :^32}\033[0m")
print(f"{'MEDIA ALUNO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
not1 = float(input("1º Nota: "))
not2 = float(input("2º Nota: "))
media = (not1 + not2)/ 2
if media < 5.0:
    print("Reprovado")
elif 5.0 <= media <= 6.9:
    print("Recuperação")
elif media >= 7.0:
    print("aprovado")