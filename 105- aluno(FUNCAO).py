print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 105 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'FUNÇÃO DEF' :^32}\033[0m")
print()
print(f"\033[32m{'ALUNO NOTA':^32}\033[0m")
print()

def nota(*num, sit=False):
    aluno_nota = dict()
    aluno_nota["total"] = len(num)
    aluno_nota["maior_nota"] = max(num)
    aluno_nota["menor_nota"] = min(num)
    aluno_nota["media"] = (sum(num)) / len(num)
    if sit:
        if aluno_nota["media"] >= 9:
            aluno_nota["situacao"] = "excellent"
        if 7 <= aluno_nota["media"] < 9:
            aluno_nota["situacao"] = "Boa"
        if 6 <= aluno_nota["media"] < 7:
            aluno_nota["situacao"] = "Razoável"
        if aluno_nota["media"] < 6:
            aluno_nota["situacao"] = "ruim"

    return aluno_nota


resp = nota(4.5, 6, 10, 9.5, sit=False)
print("resultado aluno:\n", resp)